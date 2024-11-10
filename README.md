Restaurant Management System

This project is a Restaurant Management System built using Flask, SQLAlchemy, and Bootstrap. It enables customers to view the menu and place orders, while managers and delivery agents can manage orders and track their status.

Table of Contents

	1.	Project Overview
	2.	Features
	3.	Technologies Used
	4.	Setup & Installation
	5.	Usage
	6.	Folder Structure
	8.	Future Enhancements

Project Overview

The Restaurant Management System is designed to streamline restaurant operations, allowing:
	•	Customers to view the menu and place orders.
	•	Managers to view all orders and manage order statuses.
	•	Delivery agents to view orders for delivery.

Features

	•	User Authentication: Login, registration, and OTP verification for users.
	•	Order Management: Customers can place orders; managers and agents can update and track orders.
	•	Menu Management: Dynamic menu display using SQLite database.
	•	Role-Based Access: Separate interfaces for customers, managers, and delivery agents.
	•	Bootstrap Integration: Responsive design for an enhanced user experience.

Technologies Used

	•	Flask: Backend framework to handle server logic.
	•	SQLAlchemy: ORM for database interactions with SQLite.
	•	Bootstrap: Frontend framework for responsive design.
	•	HTML/CSS: Custom templates and styles for user interface.

Setup & Installation

	1.	Clone the repository:

git clone https://github.com/your-username/restaurant-management-system.git
cd restaurant-management-system


	2.	Set up a virtual environment (optional but recommended):

python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`


	3.	Install the dependencies:


	4.	Initialize the database:

from models import Base, engine
Base.metadata.create_all(engine)


	5.	Run the application:

flask run

The app will be accessible at http://127.0.0.1:5000.

Usage

	1.	Registration & Login: Register a new user or login as an existing user. Upon successful login, customers can access the menu, and managers/delivery agents can access their dashboards.
	2.	View Menu: Customers can browse the menu and select items to place an order.
	3.	Place Orders: Customers can submit orders which will be listed under “Orders for Delivery” for delivery agents and “Manager Dashboard” for managers.
	4.	Order Confirmation: Upon placing an order, customers receive a confirmation screen.
	5.	Manager Dashboard: Managers can view all orders and update order statuses as required.
	6.	Delivery Orders: Delivery agents can view pending orders assigned to them for delivery.

Folder Structure

restaurant_system/
├── app.py                   # Main application file with routes and logic
├── models.py                # Database models with SQLAlchemy
├── templates/               # HTML files for different views
│   ├── login.html
│   ├── register.html
│   ├── otp.html
│   ├── index.html
│   ├── menu.html
│   ├── order_confirmation.html
│   ├── manager_dashboard.html
│   └── delivery_orders.html
├── static/                  
│   ├── styles.css           # Custom CSS for additional styling
└── requirements.txt         # List of dependencies for the project

Future Enhancements

	•	Order Tracking: Allow customers to track order status in real time.
	•	Inventory Management: Managers can update menu items and inventory.
	•	Notifications: Email or SMS notifications for order confirmation and delivery updates.
	•	Payment Gateway Integration: Integrate with online payment services for a seamless ordering experience.