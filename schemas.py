from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class VehicleStatus(str, Enum):
    PARKING = "PARKING"
    MOVING = "MOVING"
    IDLING = "IDLING"
    TOWING = "TOWING"

class VehicleBase(BaseModel):
    type: str
    lock_status: str
    current_speed: str
    battery_level: str
    status: VehicleStatus
    location: str
    last_updated: datetime

class VehicleCreate(VehicleBase):
    pass

class Vehicle(VehicleBase):
    vehicle_id: int

    class Config:
        orm_mode = True