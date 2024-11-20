import pytest
from app import app, db, Product, Company, Category, Blog
from datetime import datetime

@pytest.fixture
def client():
    app.config["TESTING"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory_test:"

    with app.app_context():
        db.create_all()
        yield app.test_client()
        db.drop_all()

def test_get_products(client):
    
    with app.app_context():
        company = Company(name="Test Company")
        category = Category(name="Test Category")
        product = Product(
            product_name="Test Product",
            product_model="Model X",
            price=100.0,
            description="Test Description",
            rating=4.5,
            photo_url="http://example.com/photo.jpg",
            company=company,
            category=category
        )
        db.session.add(company)
        db.session.add(category)
        db.session.add(product)
        db.session.commit()

    
    response = client.get("/products")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data["products"]) == 1
    assert data["products"][0]["product_name"] == "Test Product"

def test_create_product(client):
    with app.app_context():
        company = Company(name="Test Company")
        category = Category(name="Test Category")
        db.session.add(company)
        db.session.add(category)
        db.session.commit()
   
    response = client.post("/products", json={
        "product_name": "New Product",
        "product_model": "Model Y",
        "price": 150.0,
        "category_id": 1,
        "description": "New Description",
        "rating": 4.8,
        "photo_url": "http://example.com/new_photo.jpg",
        "company_name": "Test Company"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Product created successfully"
    assert data["product"]["product_name"] == "New Product"

def test_rate_product(client):
    with app.app_context():
        product = Product(
            product_name="Test Product",
            product_model="Model X",
            price=100.0,
            description="Test Description",
            rating=4.0,
            total_rating=8,
            rating_count=2
        )
        db.session.add(product)
        db.session.commit()

    response = client.post("/products/1/rate", json={"rating": 5})
    assert response.status_code == 200
    data = response.get_json()
    assert data["message"] == "Product rated successfully"
    assert data["product"]["average_rating"] == 4.33  # (8+5)/3

def test_create_customer(client):
    response = client.post("/customers", json={
        "first_name": "Ian",
        "last_name": "Douglass",
        "email": "Ianoh222@gmail.com",
        "password": "password",
        "address": "123 Green St",
        "phone_number": "254729839293"
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Customer created successfully"

def test_create_blog(client):
    response = client.post("/blogs", json={
        "title": "New Blog",
        "content": "This is a test blog.",
        "date_posted": datetime.utcnow().isoformat()
    })
    assert response.status_code == 201
    data = response.get_json()
    assert data["message"] == "Blog created successfully"
    assert data["blog"]["title"] == "New Blog"

def test_get_blogs(client):
    with app.app_context():
        blog = Blog(title="Sample Blog", content="This is a sample blog.", date_posted=datetime.utcnow())
        db.session.add(blog)
        db.session.commit()

    response = client.get("/blogs")
    assert response.status_code == 200
    data = response.get_json()
    assert len(data["blogs"]) == 1
    assert data["blogs"][0]["title"] == "Sample Blog"

def test_pay_mpesa(client, mocker):
    mocker.patch("app.send_money_to_phone", return_value={"status": "Success", "message": "Payment sent"})
    response = client.post("/pay/mpesa", json={
        "phone_number": "254712345678",
        "amount": 500
    })
    assert response.status_code == 200
    data = response.get_json()
    assert data["status"] == "Success"
    assert data["message"] == "Payment sent"

def test_pay_paypal(client, mocker):
    mock_payment = mocker.patch("app.paypalrestsdk.Payment", autospec=True)
    mock_payment.create.return_value = True
    mock_payment.links = [{"rel": "approval_url", "href": "http://paypal.com/approval"}]

    response = client.get("/pay/paypal")
    assert response.status_code == 302  # Strictly redirects to the Paypal approval
    assert response.location == "http://paypal.com/approval"