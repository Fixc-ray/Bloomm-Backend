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
    
    orders = db.relationship('Order', back_populates='customer', lazy='select')
    cart = db.relationship('Cart', uselist=False, back_populates='customer')


class Company(db.Model):
    __tablename__ = 'companies'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    
    products = db.relationship('Product', back_populates='company', lazy='select')


class Category(db.Model):
    __tablename__ = 'categories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    
    products = db.relationship('Product', back_populates='category', lazy='select')
    

class Product(db.Model):
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
    
    category = db.relationship('Category', back_populates='products')
    company = db.relationship('Company', back_populates='products')


class Order(db.Model):
    __tablename__ = 'orders'
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total = db.Column(db.Float, nullable=False)
    
    customer = db.relationship('Customer', back_populates='orders')


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
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())
    
    customer = db.relationship('Customer', back_populates='cart')
    items = db.relationship('CartItem', back_populates='cart', cascade='all, delete-orphan')


class CartItem(db.Model):
    __tablename__ = 'cart_items'
    
    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('carts.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    product_name = db.Column(db.String(100), nullable=False) 
    quantity = db.Column(db.Integer, nullable=False, default=1)
    price = db.Column(db.Float, nullable=False)
    
    cart = db.relationship('Cart', back_populates='items')
    product = db.relationship('Product') 
