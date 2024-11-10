from flask import Flask, render_template, redirect, url_for, request, flash, session
from models import User, MenuItem, Order, session as db_session
from functools import wraps

app = Flask(__name__)
app.secret_key = 'supersecretkey'


# Helper decorator to check if user is logged in
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            flash("Please log in to access this page.")
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function


# Helper function to check user role
def role_required(role):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            user = db_session.query(User).filter_by(id=session['user_id']).first()
            if user and user.role == role:
                return f(*args, **kwargs)
            flash("You do not have access to this page.")
            return redirect(url_for('index'))
        return decorated_function
    return wrapper


# Home route
@app.route('/')
def index():
    return render_template('index.html')


# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = db_session.query(User).filter_by(email=email, password=password).first()
        if user:
            session['user_id'] = user.id
            session['user_role'] = user.role
            return redirect(url_for('index'))
        else:
            flash("Invalid credentials")
    return render_template('login.html')


# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        new_user = User(username=username, email=email, password=password, role="Customer")
        new_user.save()
        flash("Registration successful! Please verify your OTP.")
        return redirect(url_for('otp_verification'))
    return render_template('register.html')


# OTP verification route
@app.route('/otp', methods=['GET', 'POST'])
def otp_verification():
    if request.method == 'POST':
        otp = request.form['otp']
        # OTP verification logic here
        # Assuming OTP is valid
        flash("OTP verified successfully!")
        return redirect(url_for('index'))
    return render_template('otp.html')


# Logout route
@app.route('/logout')
def logout():
    session.clear()
    flash("You have been logged out.")
    return redirect(url_for('login'))


# View menu (accessible to all logged-in users)
@app.route('/menu')
@login_required
def show_menu():
    menu_items = db_session.query(MenuItem).all()
    return render_template('menu.html', menu_items=menu_items)


# Place order (for customers)
@app.route('/order/<int:item_id>', methods=['POST'])
@login_required
def place_order(item_id):
    user_id = session.get('user_id')
    if not user_id:
        flash("You must be logged in to place an order.")
        return redirect(url_for('login'))
    new_order = Order(customer_id=user_id, status="Pending")
    new_order.save()
    flash("Order placed successfully!")
    return redirect(url_for('order_confirmation'))


# Order confirmation page
@app.route('/order_confirmation')
@login_required
def order_confirmation():
    return render_template('order_confirmation.html')


# Manager dashboard (only accessible to managers)
@app.route('/manager_dashboard')
@login_required
@role_required("Manager")
def manager_dashboard():
    orders = db_session.query(Order).all()
    return render_template('manager_dashboard.html', orders=orders)


# Delivery agent orders (only accessible to delivery agents)
@app.route('/delivery_orders')
@login_required
@role_required("DeliveryAgent")
def delivery_orders():
    orders = db_session.query(Order).filter_by(status="Pending").all()
    return render_template('delivery_orders.html', orders=orders)


if __name__ == '__main__':
    app.run(debug=True)