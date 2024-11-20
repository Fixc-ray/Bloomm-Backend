import pytest
from app import create_app, db
from app.models import Customer

@pytest.fixture(scope='module')
def app():
    """Create a test app"""
    app = create_app('testing')
    yield app
    
    db.session.remove()
    db.drop_all()

@pytest.fixture(scope='module')
def client(app):
    """Create a test client"""
    return app.test_client()

@pytest.fixture(scope='module')
def setup_database(app):
    """Setup the database"""
    with app.app_context():
        db.create_all()
    yield
    with app.app_context():
        db.drop_all()

def test_create_customer(client, setup_database):
    """Test customer creation"""
    customer = Customer(first_name="Ian", last_name="Black", email="ianblack123@gmail.com", 
                        password="password", address="CBD", phone_number="0721331234")
    with client.application.app_context():
        db.session.add(customer)
        db.session.commit()

        customer_in_db = Customer.query.filter_by(email="ianblack123@gmail.com").first()
        assert customer_in_db is not None
        assert customer_in_db.first_name == "Ian"
        assert customer_in_db.last_name == "Black"
