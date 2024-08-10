from flask import Flask, redirect, url_for, session, request, render_template
import requests

app = Flask(__name__)
app.secret_key = 'your_secret_key'

FRONTEND_URL = "http://localhost:5000/google-callback"

GOOGLE_LOGIN_URL = "https://hiring.reachinbox.xyz/api/v1/auth/google-login"

@app.route('/')
def index():
    if 'jwt_token' in session:
        return redirect(url_for('home'))
    
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return redirect(f"{GOOGLE_LOGIN_URL}?redirect_to={FRONTEND_URL}")

@app.route('/google-callback')
def google_callback():
    
    token = request.args.get('token')
    if token:
        session['jwt_token'] = token
        return redirect(url_for('home'))
    else:
        return "Login failed", 400

@app.route('/dashboard')
def dashboard():
    if 'jwt_token' not in session:
        return redirect(url_for('login'))
    
   
    return "You are logged in!"

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True) 