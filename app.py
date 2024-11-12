from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from models import db, Product, Customer
from flask_cors import CORS
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../instance/products.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = '8369a00156590593b430006a34c9944cd2f07ecbdd1caa53d259853b03fffc2dd092aa1be3c7d782efbd88949d036e1af71dbd16aba51dd308df632fb82d0632fa6a35163077ec8e3f7db1321d9dad6de5cf29a73c490a74da6f1fd14579100dc8f1e05f5003d0339739e8e2780bdeb8391d5581545da4f96cac6903c188e248309f8b67ea0ead3dc076ac02aea0ca727bae0f453f60e00f1cbe1c4e13be7d959ab041a8fb4bc5ff5e0756e70dc25a2c5dbb0f03a7d1914424a6136b51e4956ed5b4c600e8c782ae7317a9ae04d42188c4372c9816c08ec3b7f547c20cf3217188ea79a830caaa9dae4acfb628b422cd6c3522feb1d9365a8529de768cc18082'

db.init_app(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)


# User Registration
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    email = data.get('email')

    if Customer.query.filter_by(username=username).first():
        return jsonify({'message': 'Username already taken'}), 400

    if Customer.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already exists'}), 400

    hashed_password = generate_password_hash(password)
    new_user = Customer(username=username, password=hashed_password, email=email)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User registered successfully'}), 201


# User Login
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = Customer.query.filter_by(username=username).first()

    if not Customer or not check_password_hash(Customer.password, password):
        return jsonify({'message': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=Customer.user_id)
    return jsonify({
        'access_token': access_token,
        'user': {
            'username': Customer.username,
            'email': Customer.email
        }
    }), 200


if __name__ == "__main__":
    app.run(port= 5500, debug=True)