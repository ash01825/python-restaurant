from flask import Flask, render_template, redirect, url_for, request, flash
from models import User, MenuItem, Order, session

app = Flask(__name__)
app.secret_key = 'supersecretkey'

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
        user = session.query(User).filter_by(email=email, password=password).first()
        if user:
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
        return redirect(url_for('otp_verification'))
    return render_template('register.html')

# OTP verification route
@app.route('/otp', methods=['GET', 'POST'])
def otp_verification():
    if request.method == 'POST':
        otp = request.form['otp']
        # OTP verification logic here
        return redirect(url_for('index'))
    return render_template('otp.html')

# View menu
@app.route('/menu')
def show_menu():
    menu_items = session.query(MenuItem).all()
    return render_template('menu.html', menu_items=menu_items)

# Place order
@app.route('/order/<int:item_id>', methods=['POST'])
def place_order(item_id):
    new_order = Order(customer_id=1, status="Pending")  # Example with customer_id = 1
    new_order.save()
    return redirect(url_for('order_confirmation'))

# Order confirmation
@app.route('/order_confirmation')
def order_confirmation():
    return render_template('order_confirmation.html')

# Manager dashboard
@app.route('/manager_dashboard')
def manager_dashboard():
    orders = session.query(Order).all()
    return render_template('manager_dashboard.html', orders=orders)

# Delivery agent orders
@app.route('/delivery_orders')
def delivery_orders():
    orders = session.query(Order).filter_by(status="Pending").all()
    return render_template('delivery_orders.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)