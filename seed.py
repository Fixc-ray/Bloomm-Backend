from models import db, Customer, Company, Category, Product, Order
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()

    category1 = Category(name="Makeup")
    category2 = Category(name="Hair Products")
    category3 = Category(name="SkinCare")

    company1 = Company(name="Garnier")
    company2 = Company(name="L'Oreal")

    product1 = Product(
        product_name="FaceCream",
        product_model="FC100",
        price=20.00,
        category=category3,
        company=company1,
        photo_url="https://s.alicdn.com/@sc04/kf/H0e35cd60637b432a9da040648e6fc61cH.jpg_300x300.jpg"
    )

    db.session.add_all([category1, category2, category3, company1, company2, product1])
    db.session.commit()

    print("Database seeded successfully.")
