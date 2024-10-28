from flask import Flask, render_template, request, redirect, url_for, session, flash
from models import User, session as db_session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Ensure this is secure in production

# Route for the login page
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = db_session.query(User).filter_by(username=email, password=password).first()
        
        if user:
            session['user_id'] = user.id
            flash("Login successful!")
            return redirect(url_for('dashboard'))  # Redirect to the dashboard or homepage
        else:
            flash("Invalid email or password")
            return redirect(url_for('login'))
    return render_template('login.html')

# Route for the registration page
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        
        # Check if user already exists
        existing_user = db_session.query(User).filter_by(username=email).first()
        if existing_user:
            flash("User already exists. Please login.")
            return redirect(url_for('login'))
        
        # Register new user and generate OTP
        new_user = User(username=email, password=password, role='Customer')  # Assuming role as Customer
        new_user.save()
        session['otp'] = random.randint(1000, 9999)  # Simple OTP generation
        session['temp_user_id'] = new_user.id  # Temporary ID until OTP is verified
        
        flash("OTP has been sent to your email. Please verify.")
        return redirect(url_for('otp_verification'))
    return render_template('register.html')

# Route for OTP verification page
@app.route('/otp', methods=['GET', 'POST'])
def otp_verification():
    if request.method == 'POST':
        entered_otp = request.form['otp']
        
        # Check OTP correctness
        if int(entered_otp) == session.get('otp'):
            user_id = session.pop('temp_user_id', None)
            flash("Registration successful!")
            return redirect(url_for('login'))
        else:
            flash("Invalid OTP. Please try again.")
    return render_template('otp_verification.html')

if __name__ == "__main__":
    app.run(debug=True)