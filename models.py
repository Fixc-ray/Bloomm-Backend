from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy_serializer import SerializerMixin
from datetime import datetime

db = SQLAlchemy()


class Customer(db.Model):
    __tablename__ = "customers"
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    address = db.Column(db.String(120), nullable=False)
    phone_number = db.Column(db.String(15))
    
    carts = db.relationship("Cart", back_populates="customer", lazy=True)
    orders = db.relationship("Order", back_populates="customer", lazy=True)


class Company(db.Model):
    __tablename__ = "companies"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship("Product", back_populates="company", lazy=True)


class Category(db.Model):
    __tablename__ = "categories"
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    products = db.relationship("Product", back_populates="category", lazy=True)


class Product(db.Model):
    __tablename__ = "products"
    
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    product_model = db.Column(db.String(50))
    description = db.Column(db.String(1000))
    price = db.Column(db.Float, nullable=False)
    
    category = db.relationship("Category", back_populates="products", lazy=True)
    company = db.relationship("Company", back_populates="products", lazy=True)
    cart_items = db.relationship("CartItem", back_populates="product", lazy=True)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey("companies.id"), nullable=False)
    
    photo_url = db.Column(db.String(200))
    rating = db.Column(db.Float, default=0.0)
    rating_count = db.Column(db.Integer, default=0)
    total_rating = db.Column(db.Float, default=0.0)


class Order(db.Model):
    __tablename__ = "orders"
    
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    
    order_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    total = db.Column(db.Float, nullable=False)
    customer = db.relationship("Customer", back_populates="orders", lazy=True)


class Cart(db.Model):
    __tablename__ = "carts"

    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"), nullable=False)
    items = db.relationship("CartItem", back_populates="cart", lazy=True)
    customer = db.relationship("Customer", back_populates="carts")


class CartItem(db.Model):
    __tablename__ = "cart_items"

    id = db.Column(db.Integer, primary_key=True)
    cart_id = db.Column(db.Integer, db.ForeignKey("carts.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity = db.Column(db.Integer, default=1)

    cart = db.relationship("Cart", back_populates="items", lazy=True)
    product = db.relationship("Product", back_populates="cart_items", lazy=True)


class Blog(db.Model):
    __tablename__ = "blogs"
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)