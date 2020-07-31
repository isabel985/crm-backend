from . import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    user_email = db.Column(db.String, nullable=False, unique=True)
    team_id = db.Column(db.Integer, db.ForeignKey('team.team_id'))
    names = db.relationship('Name')
    companies = db.relationship('Company')

    def generate_password(self, original_password):
        self.password = generate_password_hash(original_password)
        
    def check_password(self, original_password):
        return check_password_hash(self.password, original_password)

class Team(db.Model):
    team_id = db.Column(db.Integer, primary_key=True)
    team_name = db.Column(db.String, nullable=False)
    users = db.relationship('User')

class Name(db.Model):
    name_id = db.Column(db.Integer, primary_key=True)
    name_status = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    title = db.Column(db.String)
    name_phone = db.Column(db.String)
    name_email = db.Column(db.String)
    name_city = db.Column(db.String)
    name_state = db.Column(db.String)
    name_zip_code = db.Column(db.Integer)
    company_id = db.Column(db.Integer, db.ForeignKey('company.company_id'))
    name_date_created = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    notes = db.Column(db.Text)
    resume = db.Column(db.Text)

class Company(db.Model):
    company_id = db.Column(db.Integer, primary_key=True)
    company_status = db.Column(db.String)
    company_name = db.Column(db.String)
    company_city = db.Column(db.String)
    company_state = db.Column(db.String)
    company_zip_code = db.Column(db.Integer)
    company_phone = db.Column(db.String)
    company_website = db.Column(db.String)
    company_date_created = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'))
    notes = db.Column(db.Text)
    names = db.relationship('Name')

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))