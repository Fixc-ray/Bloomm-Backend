from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = 'customers'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(15))
    
    orders = db.relationship('Order', back_populates='customer', lazy=True)


class Company(db.Model):
    __tablename__ = 'companies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship('Products', backref='company', lazy=True) 


class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship('Products', backref='category', lazy=True)
    
    
class Products(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_model = db.Column(db.String(50))
    description = db.Column(db.String(1000))
    price = db.Column(db.Float, nullable=False)
    
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)
    
    photo_url = db.Column(db.String(200))
    rating = db.Column(db.Float, default=0.0)
    rating_count = db.Column(db.Integer, default=0)
    total_rating = db.Column(db.Float, default=0.0)


class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total = db.Column(db.Float, nullable=False)
    
    customer = db.relationship('Customer', back_populates='orders', lazy=True)


class Blog(db.Model):
    __tablename__ = 'blogs'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    photo_url = db.Column(db.String(255), nullable=True) 
    

class Cart(db.Model):
    __tablename__ = 'carts'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    customer = db.relationship('Customer', backref='carts')
    
    cart_items = db.relationship('CartItem', back_populates='cart')

    def __init__(self, user_id):
        self.user_id = user_id


class CartItem(db.Model):
    __tablename__ = 'cart_items'

    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)  # ForeignKey added here
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    
    photo_url = db.Column(db.String, nullable=True)
    
    product = db.relationship('Products', backref='cart_items')  # This links to Products
    cart = db.relationship('Cart', back_populates='cart_items')

    def __init__(self, product_id, quantity, price, cart_id, photo_url=None):
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.cart_id = cart_id
        self.photo_url = photo_url

    def total(self):
        return self.price * self.quantity
