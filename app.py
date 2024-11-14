from flask import Flask, request, jsonify
from models import db, Product, Company, Category, Customer, Order, Blog
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///beauty.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

@app.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        new_user = Customer(
            username=data.get('username'),
            email=data.get('email'),
            password=data.get('password'),  
            first_name=data.get('first_name', ''),
            last_name=data.get('last_name', ''),
            address=data.get('address', ''),
            phone_number=data.get('phone_number', '')
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        db.session.rollback()  
        print(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = Customer.query.filter_by(username=data.get('username')).first()
    if user and user.check_password(data.get('password')):
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid credentials"}), 401



@app.route('/products', methods=['POST'])
def create_product():
    try:
        data = request.get_json()

        product_name = data.get('product_name')
        product_model = data.get('product_model')
        price = data.get('price')
        category_id = data.get('category_id')
        photo_url = data.get('photo_url')
        company_name = data.get('company_name')

        if not (product_name and price is not None and category_id and company_name):
            return jsonify({"error": "Missing required fields"}), 400

        if not isinstance(price, (int, float)) or price <= 0:
            return jsonify({"error": "Invalid price value"}), 400

        if not isinstance(category_id, int):
            return jsonify({"error": "Invalid category ID; must be an integer"}), 400

        # Check if the company exists or create a new one
        company = Company.query.filter_by(name=company_name).first()
        if not company:
            company = Company(name=company_name)
            db.session.add(company)
            db.session.flush()  # Ensure the company ID is generated for the new record

        # Check if the category exists
        category = Category.query.get(category_id)
        if not category:
            return jsonify({"error": "Invalid category ID"}), 400

        # Create a new product entry
        new_product = Product(
            product_name=product_name,
            product_model=product_model,
            price=price,
            category_id=category_id,
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
                "photo_url": new_product.photo_url,
                "company_name": company.name
            }
        }), 201

    except KeyError as e:
        return jsonify({"error": f"Missing key in request data: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": f"Invalid value: {str(e)}"}), 400
    except Exception as e:
        # Log the error message for debugging purposes
        db.session.rollback()
        return jsonify({"error": f"Database error: {str(e)}"}), 500


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


@app.route('/orders', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(
        customer_id=data.get('customer_id'),
        order_date=data.get('order_date'),
        total=data.get('total')
    )
    try:
        db.session.add(new_order)
        db.session.commit()
        return jsonify({"message": "Order created successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": "Database error: " + str(e)}), 500

@app.route('/blogs', methods=['POST'])
def create_blog():
    data = request.get_json()
    new_blog = Blog(
        title=data.get('title'),
        content=data.get('content'),
        date_posted=data.get('date_posted')
    )
    db.session.add(new_blog)
    db.session.commit()
    return jsonify({"message":"Blog created successfully"}), 201

if __name__ == '__main__':
    with app.app_context():
        db.create_all() 
        app.run(port=8080, debug=True)
