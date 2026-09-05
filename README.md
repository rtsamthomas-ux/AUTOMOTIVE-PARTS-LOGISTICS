# Automotive Parts Logistics

### Python + MySQL Automotive Parts Ordering and Logistics Management System

Automotive Parts Logistics is a Python-based console application connected to MySQL for managing customer information, automotive part orders, payments, workers, complaints, and demand-related records.

The project demonstrates how Python application logic can interact with a relational database to build a simple management system for an automotive parts business.

## 🚗 Overview

The application provides a menu-driven workflow for automotive parts purchasing and management.

Customers can:

- Register their details
- Select vehicle types
- Browse automotive part categories
- Select parts
- Enter quantities
- Calculate prices
- Store orders in MySQL
- View purchase information

The database also contains tables for payments, workers, complaints, and demand information.

## ✨ Features

### Customer Management

The customer workflow collects customer information and stores it in the MySQL database.

Stored customer information includes:

- Customer ID
- Name
- Phone number

### Automotive Parts Catalogue

The application contains a large predefined catalogue of automotive parts, including examples such as:

- Connecting rod
- Spark plug
- Engine blocks
- Fly wheel
- Timing belt
- Exhaust manifold
- Catalytic converter
- Exhaust pipes
- Muffler
- Oxygen sensor
- Shock absorber
- Ball joint
- Brake components
- Clutch
- Gear box
- Transmission components
- Body components
- Filters
- Cooling-system components
- Performance parts
- Safety-related components

### Vehicle-Based Pricing

The application supports different vehicle categories, including:

- Passenger Cars
- SUVs
- Trucks
- Motorcycles
- Commercial Vehicles

Pricing is adjusted using the vehicle category selected by the customer.

### Order Management

Customer orders are stored in the `order_items` table with information such as:

- Customer ID
- Product name
- Vehicle type
- Quantity
- Price

### Payment Records

The project includes a MySQL table for recording payment information such as:

- Customer ID
- Total amount
- Payment method
- Payment status

### Worker Management

The database contains a worker table designed to hold worker identifiers, passwords, and qualifications.

### Complaint and Demand Records

The project also includes tables for recording:

- Complaints associated with workers
- Product demand associated with workers

## 🏗️ Architecture

```text
                    USER
                      |
                      v
              Python Console App
                      |
          +-----------+-----------+
          |           |           |
          v           v           v
      Customer     Worker      Management
          |
          v
   Product Selection
          |
          v
    Vehicle Selection
          |
          v
   Quantity & Pricing
          |
          v
       MySQL
          |
   +------+-------+-------+-------+
   |              |       |       |
   v              v       v       v
Customers     Orders   Payments Workers
                         |
                    Complaints / Demand
```

## 🗄️ Database Design

The application creates and uses a MySQL database named:

```text
automotive_db
```

The current code creates these tables:

```text
customers
order_items
c_payments
workers
complaint
demand
```

### customers

Stores customer information.

| Column | Purpose |
|---|---|
| id | Customer identifier |
| name | Customer name |
| phone_number | Customer phone number |

### order_items

Stores individual order items.

| Column | Purpose |
|---|---|
| id | Customer/order identifier |
| product_name | Automotive part |
| vehicle_type | Selected vehicle category |
| quantity | Quantity ordered |
| price | Calculated item price |

### c_payments

Stores payment-related records.

| Column | Purpose |
|---|---|
| id | Customer identifier |
| total_amount | Total transaction amount |
| method | Payment method |
| payment_status | Payment status |

### workers

Stores worker-related information.

| Column | Purpose |
|---|---|
| Id | Worker identifier |
| password | Worker password field |
| qualification | Worker qualification |

### complaint

Stores complaint information associated with workers.

### demand

Stores product-demand information associated with workers.

## 🔄 Customer Workflow

```text
Start
  |
  v
Enter Customer Details
  |
  v
Select Part Category
  |
  v
Select Vehicle Type
  |
  v
Select Automotive Part
  |
  v
Enter Quantity
  |
  v
Calculate Price
  |
  v
Store Order in MySQL
  |
  v
Continue Shopping?
  |
  +---- Yes ----> Select More Parts
  |
  No
  |
  v
Payment / Order Completion
```

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic and console interface |
| MySQL | Persistent relational data storage |
| `mysql.connector` | Python-to-MySQL database connection |
| SQL | Database creation and CRUD operations |

## 📁 Project Structure

```text
AUTOMOTIVE-PARTS-LOGISTICS/
│
├── final code.py
└── README.md
```

The main implementation is currently contained in `final code.py`.

## ⚙️ Requirements

Before running the project, install:

- Python 3.x
- MySQL Server
- MySQL Connector/Python

Install the Python connector with:

```bash
pip install mysql-connector-python
```

## 🛠️ MySQL Setup

Make sure MySQL Server is running locally.

The current application expects a local MySQL connection and creates the database automatically if it does not already exist.

**Important:** The current source code contains a database password directly in the file. For a real project, replace this with an environment-variable or configuration-based approach and never commit real credentials to GitHub.

## ▶️ Running the Project

Clone the repository:

```bash
git clone <repository-url>
cd AUTOMOTIVE-PARTS-LOGISTICS
```

Install the dependency:

```bash
pip install mysql-connector-python
```

Update the MySQL connection settings in the application for your local environment.

Then run:

```bash
python "final code.py"
```

## 🔐 Security Notes

This repository is an educational project and should not be used as-is for production payments or authentication.

In particular:

- Do not commit real database passwords.
- Do not store plaintext passwords in a production database.
- Do not collect real payment PINs or CVVs in a console application.
- Use parameterized SQL queries consistently.
- Use environment variables or a secret manager for credentials.
- Use secure password hashing such as Argon2 or bcrypt for authentication.

## 📚 Learning Objectives

This project demonstrates practical concepts including:

- Python programming
- Functions and control flow
- Lists and dictionaries
- Input validation
- MySQL connectivity
- SQL database creation
- Table creation
- Data insertion
- Data retrieval
- Relational data management
- Basic transaction workflows

## 🧪 Current Project Status

**Status: Educational Prototype**

The application demonstrates the core concept of an automotive parts ordering and management system using Python and MySQL.

## ⚠️ Limitations

The current implementation can be improved in several areas:

- Database credentials are currently embedded in the source code.
- Password storage should be redesigned using secure hashing.
- The application is a terminal-based interface.
- Database schema relationships could be normalized further.
- IDs should use proper primary-key and auto-increment constraints.
- More comprehensive exception handling can be added.
- Automated tests are not currently included.
- Payment processing is not a real payment gateway.

## 🔮 Future Improvements

### Web Application

Build a web frontend using HTML, CSS, JavaScript, and Flask.

### Authentication

Implement secure role-based login for:

- Customers
- Workers
- Administrators

### Inventory Management

Add:

- Stock quantities
- Low-stock alerts
- Supplier management
- Inventory updates
- Purchase history

### Analytics Dashboard

Add dashboards for:

- Sales
- Revenue
- Most ordered parts
- Vehicle-based demand
- Customer activity
- Inventory levels

### API Layer

Create REST APIs so that the application can support a web or mobile frontend.

## 👨‍💻 Author

**Sam Thomas**

Computer Science Engineering Student

## 📄 License

No license is currently specified for this repository.
