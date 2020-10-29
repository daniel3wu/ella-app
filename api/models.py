from api import db, ma

# User class/model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    location = db.Column(db.String(100))

    def __init__(self, username, password, first_name, last_name, location):
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.location = location

    def __repr__(self):
        return '<User {}>'.format(self.username)

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

    def __repr__(self):
        return '<Clothing {}>'.format(self.name)

# User schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'username', 'password', 'first_name', 'last_name', 'location')

class ClothingSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'color', 'occasion', 'type')
