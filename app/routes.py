from app import app, db, login
from app.models import User, Team, Name, Company
from flask import render_template, request, jsonify
from flask_login import login_user, logout_user, current_user

@app.route('/')
def index():
    context = {'teams': Team.query.all()}
    return render_template('index.html', **context)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

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

@app.route('/companies', methods=['GET'])
def companies():
    """
    [GET] /companies
    """
    companies = Company.query.all()
    return jsonify(companies=[company.to_dict() for company in companies])

@app.route('/company/<int:company_id>', methods=['GET'])
def company(company_id):
    """
    [GET] /company/<company_id>
    """
    company = Company.query.get_or_404(company_id)
    return jsonify(company.to_dict())

@app.route('/names', methods=['GET'])
def names():
    """
    [GET] /names
    """
    names = Name.query.all()
    return jsonify(names=[name.to_dict() for name in names])

@app.route('/name/<int:name_id>', methods=['GET'])
def name(name_id):
    """
    [GET] /name/<name_id>
    """
    name = Name.query.get_or_404(name_id)
    return jsonify(name.to_dict())

@app.route('/company', methods=['POST'])
def create_company():
    """
    [POST] /company
    """
    response = request.get_json()
    c = Company(
        company_status = response['company_status'],
        company_name = response['company_name'],
        company_city = response['company_city'],
        company_state = response['company_state'],
        company_zip_code = response['company_zip_code'],
        company_phone = response['company_phone'],
        company_website = response['company_website'],
        notes = response['notes'],
        user_id = response['user_id']
    )
    c.create_company()
    return jsonify([company.to_dict() for company in Company.query.all()])

@app.route('/name', methods=['POST'])
def create_name():
    """
    [POST] /name
    """
    response = request.get_json()
    n = Name(
        name_status = response['name_status'],
        first_name = response['first_name'],
        last_name = response['last_name'],
        title = response['title'],
        name_phone = response['name_phone'],
        name_email = response['name_email'],
        name_city = response['name_city'],
        name_state = response['name_state'],
        name_zip_code = response['name_zip_code'],
        company_id = response['company_id'],
        user_id = response['user_id'],
        notes = response['notes']
    )
    n.create_name()
    return jsonify([name.to_dict() for name in Name.query.all()])

@app.route('/company/<int:company_id>', methods=['PUT'])
def update_company(company_id):
    """
    [PUT] /company/<company_id>
    """
    response = request.get_json()
    c = Company.query.get(company_id)
    c.company_status = response['company_status']
    c.company_name = response['company_name']
    c.company_city = response['company_city']
    c.company_state = response['company_state']
    c.company_zip_code = response['company_zip_code']
    c.company_phone = response['company_phone']
    c.company_website = response['company_website']
    c.notes = response['notes']
    c.user_id = response['user_id']
    db.session.commit()
    return jsonify(c.to_dict())

@app.route('/name/<int:name_id>', methods=['PUT'])
def update_name(name_id):
    """
    [PUT] /name/<name_id>
    """
    response = request.get_json()
    n = Name.query.get(name_id)
    n.name_status = response['name_status']
    n.first_name = response['first_name']
    n.last_name = response['last_name']
    n.title = response['title']
    n.name_phone = response['name_phone']
    n.name_email = response['name_email']
    n.name_city = response['name_city']
    n.name_state = response['name_state']
    n.name_zip_code = response['name_zip_code']
    n.company_id = response['company_id']
    n.notes = response['notes']
    n.user_id = response['user_id']
    db.session.commit()
    return jsonify(n.to_dict())

@app.route('/company/<int:company_id>', methods=['DELETE'])
def delete_company(company_id):
    """
    [DELETE] /company/<company_id>
    """
    c = Company.query.get(company_id)
    db.session.delete(c)
    db.session.commit()
    return jsonify([c.to_dict() for c in Company.query.all()])
    
@app.route('/name/<int:name_id>', methods=['DELETE'])
def delete_name(name_id):
    """
    [DELETE] /name/<name_id>
    """
    n = Name.query.get(name_id)
    db.session.delete(n)
    db.session.commit()
    return jsonify([n.to_dict() for n in Name.query.all()])

@app.route('/user/<int:user_id>', methods=['GET'])
def user(user_id):
    """
    [GET] /user/<user_id>
    """
    user = User.query.get_or_404(user_id)
    return jsonify(user.to_dict())