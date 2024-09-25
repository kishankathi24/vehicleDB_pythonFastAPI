from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
import database
from datetime import datetime

app = FastAPI()

# Create the database tables
models.Base.metadata.create_all(bind=database.engine)

# 1. GET /vehicles -> Get the full list of vehicles
@app.get("/vehicles", response_model=list[schemas.Vehicle])
def get_vehicles(db: Session = Depends(database.get_db)):
    vehicles = db.query(models.Vehicle).all()
    return vehicles

# 2. GET /vehicle/{vehicle_id} -> Get the details of a vehicle based on ID
@app.get("/vehicle/{vehicle_id}", response_model=schemas.Vehicle)
def get_vehicle(vehicle_id: int, db: Session = Depends(database.get_db)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.vehicle_id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")
    return vehicle

# 3. POST /vehicle/addnew -> Create a new vehicle
@app.post("/vehicle/addnew", response_model=schemas.Vehicle)
def add_new_vehicle(vehicle: schemas.VehicleCreate, db: Session = Depends(database.get_db)):
    db_vehicle = models.Vehicle(**vehicle.dict())
    db.add(db_vehicle)
    db.commit()
    db.refresh(db_vehicle)
    return db_vehicle

# 4. PUT /vehicle/{vehicle_id}/updateState -> Update vehicle details
@app.put("/vehicle/{vehicle_id}/updateState", response_model=schemas.Vehicle)
def update_vehicle(vehicle_id: int, updated_vehicle: schemas.VehicleCreate, db: Session = Depends(database.get_db)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.vehicle_id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    for key, value in updated_vehicle.dict().items():
        setattr(vehicle, key, value)

    db.commit()
    db.refresh(vehicle)
    return vehicle

# 5. DELETE /vehicle/{vehicle_id} -> Delete a vehicle
@app.delete("/vehicle/{vehicle_id}")
def delete_vehicle(vehicle_id: int, db: Session = Depends(database.get_db)):
    vehicle = db.query(models.Vehicle).filter(models.Vehicle.vehicle_id == vehicle_id).first()
    if not vehicle:
        raise HTTPException(status_code=404, detail="Vehicle not found")

    db.delete(vehicle)
    db.commit()
    return {"message": "Vehicle deleted successfully"}