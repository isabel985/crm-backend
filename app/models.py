from . import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    user_email = db.Column(db.String, nullable=False, unique=True)

    def generate_password(self, original_password):
        self.password = generate_password_hash(original_password)
        
    def check_password(self, original_password):
        return check_password_hash(self.password, original_password)

@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))