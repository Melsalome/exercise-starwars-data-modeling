from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement = True)
    name = Column(String(100), nullable=False)
    email = Column(String(250), nullable = False)
    password = Column(String(250, nullable =False))
    favorites = relationship('Favorites', back_populates='user')


class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True, autoincrement = True)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='favorites')

    characters = relationship('Characters', back_populates='favorites')
    planets = relationship('Planets', back_populates='favorites')
    vehicles = relationship('Vehicles', back_populates='favorites')

class Central_table(Base):
    __tablename__ = 'central_table'
    id = Column(Integer, primary_key = True, autoincrement = True)
    name = Column(String(100), nullable= False)
    description = Column(String(250))



class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True, autoincrement = True)
    birth_year = Column(String)
    eye_color = Column(String(100))
    hair_color = Column(String(100))
    gender = Column(String(100))
    height = Column(Integer)
    homeworld = Column(String)
    films = Column(JSON)
    mass = Column(String(250))
    skin_color = Column(String(250))
    created = Column(String(250))
    edited = Column(String(250))
    species = Column(JSON)
    starships = Column(JSON)
    url = Column(String(250))
    
    central_table_id = Column(Integer, ForeignKey('central_table.id'))
    central_table = relationship('Central_table', backref='characters')


    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship('Favorites', back_populates='characters')

    

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True, autoincrement = True)
    diameter = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(Integer)
    populations = Column(Integer)
    surface_water = Column(Integer)
    terrain = Column(String(250))

    central_table_id = Column(Integer, ForeignKey('central_table.id'))
    central_table = relationship('Central_table', backref='planets')

    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship('Favorites', back_populates='planets')


class Vehicles(Base):
    __tablename__ = 'vehicles'
    id = Column(Integer, primary_key=True, autoincrement = True)
    model = Column(String(250))
    cargo_capacity = Column(String)
    consumables = Column(String(250))
    vehicle_class = Column(String(250))
    length = Column(Integer)
    films = Column(String(250))
    cost_in_credits = Column(String(250))
    pilots = Column(String(100))

    central_table_id = Column(Integer, ForeignKey('central_table.id'))
    central_table = relationship('Central_table', backref='Vehicles')

    favorites_id = Column(Integer, ForeignKey('favorites.id'))
    favorites = relationship('Favorites', back_populates='vehicles')

def to_dict(self):
    return {}


# Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
