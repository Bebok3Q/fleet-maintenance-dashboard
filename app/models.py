from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .db import Base


class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    vin = Column(String, unique=True, index=True)
    mileage = Column(Float, default=0.0)

    diagnostics = relationship("Diagnostic", back_populates="vehicle")
    maintenance = relationship("Maintenance", back_populates='vehicle')


class Diagnostics(Base):
    __tablename__ = 'diagnostics'

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey('vehicles.id'))
    error_code = Column(String, index=False)
    description = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    vehicle = relationship("Vehicle", back_populates="diagnostics")

class Maintenance(Base):
    __tablename__ = "maintenance"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    service_type = Column(String)
    service_date = Column(DateTime, default=datetime.utcnow)
    cost = Column(Float, default=0.0)

    vehicle = relationship("Vehicle", back_populates="maintenance")