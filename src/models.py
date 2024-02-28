from sqlalchemy import ForeignKey, relationship
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


# Models Users
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80),  nullable=False)

    def __repr__(self):
        return f'<Users %r {self.id} - {self.email}>'

    def serialize(self):
        # do not serialize the password, its a security breach
        return {
            "id": self.id,
            "email": self.email,
            "pass": self.password,}


# Models Planet Favorito
class FavoritePlanets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    planets_id = db.Column(db.Integer, unique=True, nullable=False)
    users_id = db.Column(db.Integer, unique=True, nullable=False, db.ForeignKey('users.id'))
    user_to = db.relationship('Users')

    def __repr__(self):
        return f'<FavoritePlanets %r {self.id} - {self.planets_id} - {self.users_id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "planets_id": self.planets_id,
            "users_id": self.users_id}


# Models Planets
class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.Integer(25))
    rotation_period = db.Column(db.Integer(25))
    orbital_period = db.Column(db.Integer(25))
    gravity = db.Column(db.String(50))
    id_to = relationship('FavoritePlanets', foreign_keys=['FavoritePlanets.users_id'])

    def __repr__(self):
        return f'<Planets %r {self.id} - {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity}


# Models People Favorite
class FavoritePeople(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    people_id = db.Column(db.Integer, unique=True, nullable=False)
    users_id = db.Column(db.Integer, unique=True, nullable=False, ForeignKey('users.id'))
    user_to = relationship('Users', foreign_keys=['users.id'])

    def __repr__(self):
        return f'<FavoritePeople %r {self.id} - {self.people_id}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "people_id": self.planets_id,
            "users_id": self.users_id}

    

# Models People
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.Enum('Female', 'Male', name="gender"))
    height = db.Column(db.Integer(25))
    mass = db.Column(db.Integer(25))
    hair_color = db.Column(db.String(50))
    id_to = relationship('FavoritePeople', foreign_keys=['FavoritePeople.users_id'])

    def __repr__(self):
        return f'<People %r {self.id} - {self.name}>'

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "height": self.height,
            "mass": self.mass,
            "hair_color": self.hair_color}