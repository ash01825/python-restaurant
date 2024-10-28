from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', methods= ['GET', 'POST'])
def login_page():
    return render_template("login-2.html")

@app.route('/login/register')
def register_page():
    otp=OTPmanager()
    return render_template()
if __name__ == "__main__":
    app.run(debug=True)