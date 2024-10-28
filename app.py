# from flask import Flask, render_template
from models import MenuItem
# app = Flask(__name__)

# @app.route('/', methods= ['GET', 'POST'])
# def login_page():
#     return render_template("login-2.html")

# @app.route('/login/register')
# def register_page():
#     otp=OTPmanager()
#     return render_template()
# if __name__ == "__main__":
#     app.run(debug=True)
from models import MenuItem

# Fetch all items to verify
menu_items = MenuItem.get_all()
for item in menu_items:
    print(f"ID: {item.id}, Name: {item.name}, Price: {item.price}")