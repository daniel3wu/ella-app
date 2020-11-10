from api import db, ma, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

# User class/model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.String(128))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    location = db.Column(db.String(100))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def to_dict(self):
        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'location': self.location
        }

        return data

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class Clothing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    color = db.Column(db.String(100))
    occasion = db.Column(db.String(100))
    type = db.Column(db.String(100))

    def __init__(self, name, color, occasion, type):
        self.name = name
        self.color = color
        self.occasion = occasion
        self.type = type

class Outfit(db.Model):
    name = db.Column(db.String(100), primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('user.username'), primary_key=True)
    top_id = db.Column(db.Integer, db.ForeignKey('clothing.id'))
    bottom_id = db.Column(db.Integer, db.ForeignKey('clothing.id'))

class Matches(db.Model):
    clothing_id1 = db.Column(db.Integer, db.ForeignKey('clothing.id'), primary_key=True)
    clothing_id2 = db.Column(db.Integer, db.ForeignKey('clothing.id'), primary_key=True)

class Belongs(db.Model):
    clothing_id = db.Column(db.Integer, db.ForeignKey('clothing.id'), primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('user.username'))

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name', 'location')

class OutfitSchema(ma.Schema):
    class Meta:
        fields = ('name', 'username', 'top_id', 'bottom_id', 'last_name', 'location')

class ClothingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'color', 'occasion', 'type')

class MatchesSchema(ma.Schema):
    class Meta:
        fields = ('clothing_id1', 'clothing_id2')

class BelongsSchema(ma.Schema):
    class Meta:
        fields = ('clothing_id', 'username')
