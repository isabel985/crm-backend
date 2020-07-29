from app import app, db, login
from app.models import User
from flask import render_template, request
from flask_login import login_user

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        remember_me = request.form.get('remember_me')

        user = User.query.filter_by(email=email).first()
        if user is None or not user.check_password(password):
            flash('Either your email address or password is incorrect. Try again.', 'warning')
            return redirect(url_for('login'))
        login_user(user, remember=remember_me)
        flash('User logged in successfully.', 'info')
        return redirect(url_for('index'))
    return render_template('login.html')

@app.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out successfully.', 'info')
    return redirect(url_for('login'))