from app import app, db, login
from app.models import User, Team, Name, Company
from flask import render_template, request
from flask_login import login_user, logout_user, current_user

@app.route('/')
def index():
    context = {'teams': Team.query.all()}
    return render_template('index.html', **context)

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

@app.route('/add_name', methods=['GET', 'POST'])
def add_name():
    if request.method == 'POST':
        name_status = request.form.get('name_status')
        first_name = request.form.get('first_name')
        last_name = request.form.get('last_name')
        title = request.form.get('title')
        name_phone = request.form.get('name_phone')
        name_email = request.form.get('name_email')
        name_city = request.form.get('name_city')
        name_state = request.form.get('name_state')
        name_zip_code =request.form.get('name_zip_code')
        notes = request.form.get('notes')
        resume = request.form.get('resume')

        email_to_find = Name.query.filter_by(email=email).first()
        if email_to_find is not None:
            flash('Email already exists.', 'danger')
            return redirect(url_for('add_name'))
        else:
            n = Name(name_status=name_status, first_name=first_name, last_name=last_name, title=title, name_phone=name_phone, name_email=name_email, name_city=name_city, name_state=name_state, name_zip_code=name_zip_code, notes=notes, resume=resume, user_id=current_user.id)
            
            # need to add company id
            
            db.session.add(n)
            db.session.commit()
            flash('Name was successfully created', 'success')
            return redirect(url_for('add_name'))
    return render_template(url_for('index'))

@app.route('/add_company', methods=['GET', 'POST'])
def add_company():
    if request.method == 'POST':
        company_status = request.form.get('company_status')
        company_name = request.form.get('company_name')
        company_city = request.form.get('company_city')
        company_state = request.form.get('company_state')
        company_zip_code =request.form.get('company_zip_code')
        company_phone = request.form.get('company_phone')
        company_website = request.form.get('company_website')
        notes = request.form.get('notes')

        # figure out how to view names under companies

        company_to_find = Name.query.filter_by(company_phone=company_phone).first()
        if company_to_find is not None:
            flash('Company already exists.', 'danger')
            return redirect(url_for('add_company'))
        else:
            c = Company(company_status=company_status, company_name=company_name, company_city=company_city, company_state=company_state, company_zip_code=company_zip_code, company_phone=company_phone, company_website=company_website, notes=notes, user_id=current_user.id)
            db.session.add(c)
            db.session.commit()
            flash('Company was successfully created', 'success')
            return redirect(url_for('add_company'))
    return render_template(url_for('index'))
