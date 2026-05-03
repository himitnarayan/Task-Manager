from flask_login import UserMixin
from bson.objectid import ObjectId
from app import bcrypt
from app.db import get_db

class User(UserMixin):
    def __init__(self, email, password_hash, role='Member', _id=None):
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self._id = _id

    def get_id(self):
        return str(self._id)

    @staticmethod
    def create(email, password, role='Member'):
        db = get_db()
        hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
        user_data = {
            'email': email,
            'password_hash': hashed_password,
            'role': role
        }
        result = db.users.insert_one(user_data)
        return User(email, hashed_password, role, result.inserted_id)

    @staticmethod
    def get_by_email(email):
        db = get_db()
        user_data = db.users.find_one({'email': email})
        if user_data:
            return User(
                email=user_data['email'],
                password_hash=user_data['password_hash'],
                role=user_data.get('role', 'Member'),
                _id=user_data['_id']
            )
        return None

    @staticmethod
    def get_by_id(user_id):
        db = get_db()
        try:
            user_data = db.users.find_one({'_id': ObjectId(user_id)})
            if user_data:
                return User(
                    email=user_data['email'],
                    password_hash=user_data['password_hash'],
                    role=user_data.get('role', 'Member'),
                    _id=user_data['_id']
                )
        except:
            pass
        return None

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password_hash, password)
