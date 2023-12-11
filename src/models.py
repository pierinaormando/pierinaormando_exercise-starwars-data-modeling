import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Planet(Base):
    __tablename__= 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String (20), unique=True)
    population = Column(Integer)
    diameter = Column(Integer)

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), unique=True)
    height = Column(Float)
    mass = Column(Integer)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

class Vehicle(Base):
    __tablename__= 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(40), unique=True)
    model = Column(String(40))
    passenger = Column(Integer)

class VehiclePilots(Base):
    __tablename__= 'vehiclePilots'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    character = relationship(Character)
    vehicle = relationship(Vehicle)

class FavoritesVehicles(Base):
    __tablename__= 'favoritesVehicles'
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    vehicle = relationship(Vehicle)

class FavoritesPlanets(Base):
    __tablename__= 'favoritesPlanets'
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer, ForeignKey('planet.id'))
    planet = relationship(Planet)

class FavoritesCharacters(Base):
    __tablename__= 'favoritesCharacters'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    character = relationship(Character)
    
## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
