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
    users = db.relationship('User', backref='author', lazy='dynamic')

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

    def to_dict(self):
        data = {
            'name_id': self.name_id,
            'name_status': self.name_status,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'title': self.title,
            'name_phone': self.name_phone,
            'name_email': self.name_email,
            'name_city': self.name_city,
            'name_state': self.name_state,
            'name_zip_code': self.name_zip_code,
            'company_id': self.company_id,
            'name_date_created': self.name_date_created,
            'user_id': self.user_id,
            'notes': self.notes,
            'resume': self.resume
        }
        return data
    
    def from_dict(self, data):
        for field in ['name_status', 'first_name', 'last_name', 'title', 'name_phone', 'name_email', 'name_city', 'name_state', 'name_zip_code', 'company_id', 'user_id' 'notes', 'resume']:
            if field in data:
                setattr(self, field, data[field])

    def create_name(self):
        db.session.add(self)
        db.session.commit()

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
    names = db.relationship('Name', backref='author', lazy='dynamic')

    def to_dict(self):
        data = {
            'company_id': self.company_id,
            'company_status': self.company_status,
            'company_name': self.company_name,
            'company_city': self.company_city,
            'company_state': self.company_state,
            'company_zip_code': self.company_zip_code,
            'company_phone': self.company_phone,
            'company_website': self.company_website,
            'company_date_created': self.company_date_created,
            'user_id': self.user_id,
            'notes': self.notes,
            'names': [n.to_dict() for n in self.names.all()]
        }
        return data

    def from_dict(self, data):
        for field in ['company_status', 'company_name', 'company_city', 'company_state', 'company_zip_code', 'company_phone', 'company_website', 'user_id', 'notes', 'names']:
            if field in data:
                setattr(self, field, data[field])

    def create_company(self):
        db.session.add(self)
        db.session.commit()

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))