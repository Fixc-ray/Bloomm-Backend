<div style= "text-align: center;">
<img src="Bloom-Beauty.png" alt="Bloom Beauty Logo" width="210" height="210"
></img>
</div>


![Contributors](https://img.shields.io/github/contributors/Fixc-ray/Bloomm-Backend)
![Forks](https://img.shields.io/github/forks/Fixc-ray/Bloomm-Backend)
![Stars](https://img.shields.io/github/stars/Fixc-ray/Bloomm-Backend)
![License](https://img.shields.io/github/license/Fixc-ray/Bloomm-Backend)
![Issues](https://img.shields.io/github/issues/Fixc-ray/Bloomm-Backend)


# Bloom Beauty Backend
Welcome to the Back back side of Boom Beauty, the Backend :). 

This project manages the core business logic for the beauty store, handling product management, customer accounts, order payments, and blogs.

## Features
- **Product Management**: Add, update, delete, and rating products.
- **Customer Management**: Registering new customers and managing  their profiles.
- **Order Management**: Managing customer orders and their statuses.
- **Blog Management**: Create, read, and manage blog posts for the store.
- **Payment Integration**: Handle payments via M-Pesa and PayPal.

## REquirements
- Python 3.10+
- Flask
- SQLAlchemy
- PayPal SDK
- M-Pesa API (configured in mpesa.py)

## Installation
1. Clone the repository:

git clone 
```
git@github.com:Fixc-ray/Bloomm-Backend.git
```

then cd into `Bloom-Backend`.

2. Install the required dependencies:

```
pipenv install
```
or
```
pip install -r requirements.txt
```

3. Set up your environment variables. Create a `.env` file and configure the PayPal API credentials:
```
PAYPAL_CLIENT_ID = your-client-id
PAYPAL_CLIENT_SECRET = your-client-secret
```

4. Run the application:
```
python app.py
```
or
```
python3 app.py
```

The Backend will start running locally on `http://localhost:5000`.
------


# The Features Breakdown

1. __Product Management__

- Adds a new Product:
Uses the Backend to add new beauty products to the store, including its details like the name, price, description, and image URL.

- Updates the Product:
Updates product details such as the price, description, and images.

- Delete Product:
Removes a product from the store inventory.

- Rate Product:
Customers can rate a product, which helps other customers make purchasing decisions.

2. __Customer Management__

- Register New Customer:
Customers can create an account by providing basic details like name, email, password, and contact information.

- Customer Profile:
Customers can view and update their profile information.

3. __Order Management__

- Create Order:
After adding products to the cart, customers can place an order.

- Tracking Orders:
Customers can check the status of their orders.

- Order History:
Customers can view their past orders.

4. __Blog Management__

- Create Blog:
Admins () can create blog posts to keep their known clients and other customers informed about new products, trends, or beauty tips.

- Manage Blogs:
Edit or delete blog posts.

5. __Payment Integration__

- M-Pesa Payments:
Customers can pay for orders via M-Pesa using an integrated API.

- PayPal Payments:
Customers can use PayPal for online payments after placing an order.


## Database Models
This backend uses SQLAlchemy with SQLite (or another relational database) to manage the following models:

- __Customer__: Stores customer details like name, email, and password.

- __Product__: Stores information about products like name, price, category, description, and images.

- __Order__: Stores order details including products, order status, and customer information.

- __Blog__: Stores blog posts written by admins.

- __Payment__: Stores payment details for both M-Pesa and PayPal transactions.


## Running the Application

1. Ensure the environment is set up correctly with all dependencies installed.

2. Run the application with:

```bash
python app.py
```

3. The application will be available at `http://localhost:5000`. 

- You can use tools like `Postman` or a `Frontend` to interact with the backend.
____


## Challenges

- Developing the Backend presented several challenges, ranging from technical obstacles to collaborative issues.

- Here are some challenges we faced as a group:
1. Database Design

- Challenge: Designing an efficient and scalable database schema.
- Resolution: Iterative design and testing ensured an optimal structure for data relationships and retrievals.

2. API Endpoint Design
- Challenge: Balancing simplicity, functionality, and consistency in the API endpoints we wanted to use.
- Misaligned API design could lead to a confusing developer experience for frontend integration.

- Resolution: Adhering to RESTful principles and documenting endpoints in detail.

3. Error Handling
Challenge: Ensuring consistent and meaningful error messages for various failure scenarios.
Resolution: Standardizing error responses handle exceptions gracefully.

4. Authentication and Security
- Challenge: Implementing secure authentication mechanisms like JWT, session management, and data encryption.
- Any weak security measures could expose sensitive user data to vulnerabilities/hackers.

- Resolution: Leveraging libraries for encryption and regular code reviews to identify and mitigate risks.

5. Testing and Debugging
- Challenge: We wrote exhaustive tests to cover edge cases and debugging issues in complex flows.
- Since Bugs in critical functionality could go unnoticed they could have caused disruptions post-deployment.
- Resolution: Adopting test-driven development (TDD) and leveraging tools like Postman for API testing.

By overcoming these challenges, our group gained valuable experience and insights into backend development, improving both their technical expertise and collaborative efficiency. These obstacles also reinforced the importance of proactive planning and communication within the team.


## Future enhancements
1. Performance Optimization
We want to optimize API responses and query performance under load due to high latency or server crashes during high traffic could degrade the user experience.


## Contributions

To contribute to this project, fork the repository and submit a pull request with your changes.

### NOTE BY
- This backend does NOT expose an API endpoint for external access but is instead intended to power the store's internal logic (e.g., via a web frontend).

- The backend handles all the business logic, database management, and payment integrations.
----

- The Backend was coded and compiled by:

<a href="https://github.com/Fixc-ray" title="Justin Ray's Profile">
  <img src="https://avatars.githubusercontent.com/Fixc-ray" alt="Ray's Profile Picture" width="90" height="90" style="border-radius: 50%;"/>
Justin Ray</a>

<a href="https://github.com/Margaret617" title="Margaret's Profile">
  <img src="https://avatars.githubusercontent.com/Margaret617" alt="Margaret's Profile Picture" width="90" height="90" style="border-radius: 50%;"/>
Margaret</a>

<a href="https://github.com/Umbrellaisnothere" title="Keith Murimi's Profile">
  <img src="https://avatars.githubusercontent.com/Umbrellaisnothere" alt="Keith's Profile Picture" width="90" height="90" style="border-radius: 50%;"/>
Keith Murimi</a>