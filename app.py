from flask import Flask, request, jsonify, render_template, redirect
from flask_cors import CORS
from models import db, Products, Company, Category, Customer, Order, Blog, Cart, CartItem
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token
import traceback
from mpesa import send_money_to_phone
import requests
import paypalrestsdk
from dotenv import load_dotenv
load_dotenv()
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os


app = Flask(__name__)
CORS(app)  # Enable CORS for all routes and origins
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beauty.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '972005679905596ccd4ed314bc98c944b88006d2bf5b229b4b04ee41b16159d0076ae05d861cf5b2d5bcc6f5057965096bb96659705c64738cf404737e6ac26b3f2422a89c12bd7d939163c20db680db25712b75de060dd668319ed57ef56c06172c82913abc4554fbe8107b860e23bcb65097b302200500c7341a720076e62ecf562bec94a8b75941f62c1faa038b2bbcd1896a9f3e42582b86e3dfe83ddc6bd103fc79229f5cb294742d47c9c3a15ebb5e7dea2b9deaddb174772595808b5abc704187316ac8a74b2adb451c3c1f0292126eb28ecd7ecc1c2f6c59177f3e8b0f115b4d027a9d386f131a803c6b5958e99d911b0cc730d0cd0e4bbe523462b4bf994225883c97589d6e8b298533a4e3f633089986c13035deafe9f865bfd0d4'

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)


@app.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        first_name = data.get('first_name')
        password = data.get('password')
        email = data.get('email')

        if not first_name or not password or not email:
            return jsonify({'message': 'All fields are required'}), 400

        if Customer.query.filter_by(first_name=first_name).first():
            return jsonify({'message': 'first_name already taken'}), 400

        if Customer.query.filter_by(email=email).first():
            return jsonify({'message': 'Email already exists'}), 400

        hashed_password = generate_password_hash(password)
        new_user = Customer(first_name=first_name, password=hashed_password, email=email)

        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'Customer registered successfully'}), 201
    except Exception as e:
        print("Error occurred:", str(e))
        traceback.print_exc()
        return jsonify({'message': 'Internal server error'}), 500
    
    
@app.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        first_name = data.get('first_name')
        password = data.get('password')

        if not first_name or not password:
            return jsonify({'message': 'Both fields are required'}), 400

        user = Customer.query.filter_by(first_name=first_name).first()

        if not user or not check_password_hash(user.password, password):
            return jsonify({'message': 'Invalid credentials'}), 401

        access_token = create_access_token(identity=user.user_id)
        return jsonify({
            'access_token': access_token,
            'user': {
                'first_name': user.first_name,
                'email': user.email
            }
        }), 200
    except Exception as e:
        print("Error occurred:", str(e))
        traceback.print_exc()
        return jsonify({'message': 'Internal server error'}), 500


@app.route('/products', methods=['POST'])
def create_product():
    data = request.get_json()

    product_name = data.get('product_name')
    product_model = data.get('product_model')
    price = data.get('price')
    category_id = data.get('category_id')
    description = data.get('description', '')
    rating = data.get('rating')
    photo_url = data.get('photo_url')
    company_name = data.get('company_name')

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
        new_product = Products(
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


@app.route('/products', methods=['GET'])
def get_products():
    products = Products.query.all()
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


@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = Products.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    data = request.get_json()
    product.product_name = data.get('product_name', product.product_name)
    product.product_model = data.get('product_model', product.product_model)
    product.price = data.get('price', product.price)
    product.category_id = data.get('category_id', product.category_id)
    product.company_id = data.get('company_id', product.company_id)
    product.description = data.get('description', product.description)
    product.rating = data.get('rating', product.rating)
    product.photo_url = data.get('photo_url', product.photo_url)

    db.session.commit()
    return jsonify({"message": "Product updated successfully"}), 200


@app.route('/cart', methods=['GET'])
def get_cart():
    """Return the current cart contents."""
    # Get the current user (you would typically fetch this from session or authentication)
    customer_id = 1  # Assume this is coming from the authenticated user
    cart = Cart.query.filter_by(customer_id=customer_id).first()
    if not cart:
        return jsonify({"cart": []})

    cart_items = [{
        'id': item.product.id,
        'name': item.product.product_name,
        'price': item.product.price,
        'quantity': item.quantity
    } for item in cart.items]

    return jsonify({"cart": cart_items})


@app.route('/cart', methods=['POST'])
def add_to_cart():
    """Add an item to the cart."""
    data = request.json
    product_id = data.get('id')
    quantity = data.get('quantity')

    if not product_id or not quantity or quantity <= 0:
        return jsonify({"error": "Invalid item data"}), 400

    # Get the current customer (this is assumed to come from the session or authentication)
    customer_id = 1  # This should come from session or user context
    customer = Customer.query.get(customer_id)
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    # Find the product
    product = Products.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    # Get or create the cart for the customer
    cart = Cart.query.filter_by(customer_id=customer_id).first()
    if not cart:
        cart = Cart(customer_id=customer_id)
        db.session.add(cart)
        db.session.commit()

    # Check if item already exists in the cart
    cart_item = CartItem.query.filter_by(cart_id=cart.id, product_id=product_id).first()
    if cart_item:
        cart_item.quantity += quantity
    else:
        cart_item = CartItem(cart_id=cart.id, product_id=product_id, quantity=quantity)
        db.session.add(cart_item)

    db.session.commit()
    return jsonify({"message": "Item added to cart", "cart": get_cart()})


@app.route('/cart/<int:item_id>', methods=['PUT'])
def update_cart_item(item_id):
    """Update the quantity of an item in the cart."""
    quantity = request.json.get('quantity')
    if not quantity or quantity <= 0:
        return jsonify({"error": "Invalid quantity"}), 400

    cart_item = CartItem.query.get(item_id)
    if not cart_item:
        return jsonify({"error": "Item not found in cart"}), 404

    cart_item.quantity = quantity
    db.session.commit()
    return jsonify({"message": "Item updated", "cart": get_cart()})


@app.route('/cart/<int:item_id>', methods=['DELETE'])
def remove_from_cart(item_id):
    """Remove an item from the cart."""
    cart_item = CartItem.query.get(item_id)
    if not cart_item:
        return jsonify({"error": "Item not found in cart"}), 404

    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({"message": "Item removed", "cart": get_cart()})


@app.route('/cart/clear', methods=['DELETE'])
def clear_cart():
    """Clear all items from the cart."""
    # Clear all items from the cart
    customer_id = 1  # Assume customer_id is retrieved from session or context
    cart = Cart.query.filter_by(customer_id=customer_id).first()
    if cart:
        db.session.delete(cart)
        db.session.commit()
    
    return jsonify({"message": "Cart cleared"})


@app.route('/customers', methods=['POST'])
def create_customer():
    data = request.get_json()
    new_customer = Customer(
        first_name=data.get('first_name'),
        last_name=data.get('last_name'),
        email=data.get('email'),
        password=data.get('password'),
        address=data.get('address'),
        phone_number=data.get('phone_number')
    )
    try:
        db.session.add(new_customer)
        db.session.commit()
        return jsonify({"message": "Customer created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error: " + str(e)}), 500


@app.route('/blogs', methods=['POST'])
def create_blog():
    try:
        data = request.get_json()
        title = data.get('title')
        content = data.get('content')
        date_posted = data.get('date_posted', datetime.utcnow())
        photo_url = data.get('photo_url', '')

        if isinstance(date_posted, str):
            date_posted = datetime.fromisoformat(date_posted)

        if not title or not content:
            return jsonify({"error": "Missing required fields"}), 400
        
        new_blog = Blog(
            title=title,
            content=content,
            date_posted=date_posted,
            photo_url=photo_url 
        )
        
        db.session.add(new_blog)
        db.session.commit()
        
        return jsonify({
            "message": "Blog created successfully", 
            "blog": {
                "title": new_blog.title,
                "content": new_blog.content,
                "date_posted": new_blog.date_posted,
                "photo_url": new_blog.photo_url 
            }
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error: " + str(e)}), 500

    
@app.route('/blogs', methods=['GET'])
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

    
@app.route('/products/<int:product_id>/rate', methods=['POST'])
def rate_product(product_id):
    product = Products.query.get(product_id)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    
    data = request.get_json()
    new_rating = data.get('rating')
    
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


@app.route('/pay/mpesa', methods=['POST'])
def payMpesa():
    data = request.get_json()
    print("Received data:", data)

    phone_number = data.get('phone_number')
    amount = data.get('amount')

    if not phone_number or not amount:
        return jsonify({"error": "Missing phone number or amount"}), 400

    try:
        response = send_money_to_phone(phone_number, amount)
        print("M-Pesa response:", response)

        if response and "Message" in response:
            return jsonify(response), 200
        else:
            return jsonify({"error": "M-Pesa response is invalid or empty", "response": response}), 500

    except requests.exceptions.RequestException as e:
        print("Request to M-Pesa failed:", e) 
        return jsonify({"error": "Payment failed", "details": str(e)}), 500
    except Exception as e:
        print("General exception:", e)
        return jsonify({"error": "An unexpected error occurred", "details": str(e)}), 500


@app.route('/callback', methods=['POST'])
def callback():
    """Handle callback from M-Pesa."""
    data = request.get_json()
    print('Callback received:', data)
    return jsonify({"ResultCode": 0, "ResultDesc": "Success"})


@app.route('/pay/paypal', methods=['GET'])
def payPaypal():
    # Create a payment object
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
                    "price": "10.00",  # Replace with cart total price
                    "currency": "USD",
                    "quantity": 1
                }]
            },
            "amount": {
                "total": "10.00",  # Replace with cart total price
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


@app.route('/payment/execute', methods=['GET'])
def execute_payment():
    payment_id = request.args.get('paymentId')
    payer_id = request.args.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return "Payment executed successfully"
    else:
        return jsonify({"error": payment.error})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)), debug=True)
