from flask import Flask, request, jsonify, render_template, redirect, request, sessions
from flask_migrate import Migrate
from flask_session import Session
from flask_cors import CORS
from models import db, Product, Company, Category, Customer, Order, Blog, Cart, CartItem
from dotenv import load_dotenv
from datetime import datetime
from mpesa import send_money_to_phone
import paypalrestsdk
import requests
import os

load_dotenv()

PAYPAL_BASE_URL = "https://sandbox.paypal.com"
PAYPAL_CLIENT_ID = os.getenv("PAYPAL_CLIENT_ID")
PAYPAL_CLIENT_SECRET = os.getenv("PAYPAL_CLIENT_SECRET")

if not PAYPAL_CLIENT_ID or not PAYPAL_CLIENT_SECRET:
    raise ValueError("PayPal Client ID and Secret are not set!")

paypalrestsdk.configure({
    "mode": "sandbox",  
    "client_id": os.getenv("PAYPAL_CLIENT_ID"),
    "client_secret": os.getenv("PAYPAL_CLIENT_SECRET")
    # "client_id": PAYPAL_CLIENT_ID,
    # "client_secret": PAYPAL_CLIENT_SECRET
})


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///beauty.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route("/")
def index():
    return render_template("home.html")


@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    product_list = []
    for product in products:
        product_data = {
            "id": product.id,
            "product_name": product.product_name,
            "product_model": product.product_model,
            "price": product.price,
            "category_id": product.category_id,
            "description": product.description,
            "rating": product.rating,
            "photo_url": product.photo_url,
            "company_name": product.company.name
        }
        product_list.append(product_data)
    return jsonify({"products": product_list}), 200


@app.route("/products", methods=["POST"])
def create_product():
    data = request.get_json()
    
    product_name = data.get("product_name")
    product_model = data.get("product_model")
    price = data.get("price")
    category_id = data.get("category_id")
    description = data.get("description", "")
    rating = data.get("rating")
    photo_url = data.get("photo_url")
    company_name = data.get("company_name")

    if not (product_name and price and category_id and company_name):
        return jsonify({"error": "Missing required fields"}), 400

    company = Company.query.filter_by(name=company_name).first()
    if not company:
        company = Company(name=company_name)
        db.session.add(company)
    
    category = Category.query.get(category_id)
    if not category:
        return jsonify({"error": "Invalid category ID"}), 400
    
    try:
        new_product = Product(
            product_name=product_name,
            product_model=product_model,
            price=price,
            category_id=category_id,
            description=description, 
            rating=rating,
            photo_url=photo_url,
            company_id=company.id
        )
        
        db.session.add(new_product)
        db.session.commit()

        return jsonify({
            "message": "Product created successfully",
            "product": {
                "product_name": new_product.product_name,
                "product_model": new_product.product_model,
                "price": new_product.price,
                "category_id": new_product.category_id,
                "description": new_product.description, 
                "rating": new_product.rating,
                "photo_url": new_product.photo_url,
                "company_name": company.name
            }
        }), 201
    
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error: " + str(e)}), 500


@app.route("/products/<int:product_id>/rate", methods=["POST"])
def rate_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    data = request.get_json()
    new_rating = data.get("rating")
    
    if not (0 <= new_rating <= 5):
        return jsonify({"error": "Rating must be between 0 and 5"}), 400
    
    product.total_rating += new_rating
    product.rating_count += 1 
    
    product.rating = product.total_rating / product.rating_count
    
    try:
        db.session.commit()
        return jsonify({"message": "Product rated successfully", "product": {
            "id": product.id,
            "product_name": product.product_name,
            "average_rating": product.rating,
            "total_rating": product.total_rating
        }
                        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to update rating:{str(e)}"}), 500


@app.route("/products/<int:product_id>", methods=["PUT"])
def update_product(product_id):
    product = Product.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    product.product_name = data.get("product_name", product.product_name)
    product.product_model = data.get("product_model", product.product_model)
    product.price = data.get("price", product.price)
    product.category_id = data.get("category_id", product.category_id)
    product.company_id = data.get("company_id", product.company_id)
    product.description = data.get("description", product.description)
    product.rating = data.get("rating", product.rating)
    product.photo_url = data.get("photo_url", product.photo_url)

    db.session.commit()
    return jsonify({"message": "Product updated successfully"}), 200


@app.route("/customers", methods=["POST"])
def create_customer():
    data = request.get_json()
    new_customer = Customer(
        first_name=data.get("first_name"),
        last_name=data.get("last_name"),
        email=data.get("email"),
        password=data.get("password"),
        address=data.get("address"),
        phone_number=data.get("phone_number")
    )
    try:
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({"message": "Customer created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error: " + str(e)}), 500


@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    new_order = Order(
        customer_id=data.get("customer_id"),
        order_date=data.get("order_date"),
        total=data.get("total")
    )
    try:
        db.session.add(new_order)
        db.session.commit()
        return jsonify({"message": "Order created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error: " + str(e)}), 500


@app.route("/blogs", methods=["GET"])
def get_blogs():
    blogs = Blog.query.all()
    blog_list = []
    for blog in blogs:
        blog_data = {
            "id": blog.id,
            "title": blog.title,
            "content": blog.content,
            "date_posted": blog.date_posted
        }
        blog_list.append(blog_data)
    return jsonify({"blogs": blog_list}), 200


@app.route("/blogs", methods=["POST"])
def create_blog():
    try:
        data = request.get_json()
        title = data.get("title")
        content = data.get("content")
        date_posted = data.get("date_posted", datetime.utcnow())

        if isinstance(date_posted, str):
            date_posted = datetime.fromisoformat(date_posted)

        if not title or not content:
            return jsonify({"error": "Missing required fields"}), 400
        
        new_blog = Blog(
            title=title,
            content=content,
            date_posted=date_posted
        )
        
        db.session.add(new_blog)
        db.session.commit()
        return jsonify({"message": "Blog created successfully", "blog": {
            "title": new_blog.title,
            "content": new_blog.content,
            "date_posted": new_blog.date_posted
        }}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error: " + str(e)}), 500


@app.route("/pay/mpesa", methods=["POST"])
def payMpesa():
    data = request.get_json()
    print("Received data:", data)  

    phone_number = data.get("phone_number")
    amount = data.get("amount")

    if not phone_number or not amount:
        return jsonify({"error": "Missing phone number or amount"}), 400

    try:
        response = send_money_to_phone(phone_number, amount)
        print("M-Pesa response:", response)  
        return jsonify(response), 200
    except request.exceptions.RequestException as e:
        print("Request exception:", e)  
        return jsonify({"error": "Payment failed", "details": str(e)}), 500
    except Exception as e:
        print("General exception:", e)  
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.route("/pay/paypal", methods=["GET"])
def payPaypal():
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": "http://localhost:5000/payment/execute",
            "cancel_url": "http://localhost:5000/"
        },
        "transactions": [{
            "item_list": {
                "items": [{
                    "name": "Cart Items",
                    "sku": "001",
                    "price": "15.00",
                    "currency": "USD",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": "15.00",
                "currency": "USD"
            },
            "description": "Payment for items in the cart"
        }]
    })

    if payment.create():
        print("Payment created successfully")
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)
    else:
        return jsonify({"error": payment.error})


@app.route("/callback", methods=["POST"])
def callback():
    """Handle callback from M-Pesa."""
    data = request.get_json()
    print("Callback received:", data)
    return jsonify({"ResultCode": 0, "ResultDesc": "Success"})


@app.route("/payment/execute", methods=["GET"])
def execute_payment():
    payment_id = request.args.get("paymentId")
    payer_id = request.args.get("PayerID")

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return "Payment executed successfully"
    else:
        return jsonify({"error": payment.error})
    


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(port= 5500, debug=True)