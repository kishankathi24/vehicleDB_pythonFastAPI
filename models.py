from sqlalchemy import Column, Integer, String, Enum, DateTime
from database import Base
import enum

class VehicleStatus(enum.Enum):
    PARKING = "PARKING"
    MOVING = "MOVING"
    IDLING = "IDLING"
    TOWING = "TOWING"

class Vehicle(Base):
    __tablename__ = "vehicles"

    vehicle_id = Column(Integer, primary_key=True, index=True)
    type = Column(String(50), nullable=False)
    lock_status = Column(String(10), nullable=False)
    current_speed = Column(String(10), nullable=False)
    battery_level = Column(String(10), nullable=False)
    status = Column(Enum(VehicleStatus), nullable=False)
    location = Column(String(50), nullable=False)
    last_updated = Column(DateTime, nullable=False)