from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import Maintenance, Vehicle
from ..schemas import MaintenanceCreate, MaintenanceResponse

router = APIRouter()

@router.post("/maintenance/", response_model=MaintenanceResponse)
def create_maintenance(maintenance: MaintenanceCreate, db: Session = Depends(get_db)):
    if not db.query(Vehicle).filter(Vehicle.id == maintenance.vehicle_id).first():
        raise HTTPException(status_code=404, detail="Vehicle not found")

    db_maintenance = Maintenance(**maintenance.dict())
    db.add(db_maintenance)
    db.commit()
    db.refresh(db_maintenance)
    return db_maintenance

@router.get("/maintenance/{maintenance_id}", response_model=MaintenanceResponse)
def get_maintenance(maintenance_id: int, db: Session = Depends(get_db)):
    maintenance = db.query(Maintenance).filter(Maintenance.id == maintenance_id).first()
    if not maintenance:
        raise HTTPException(status_code=404, detail="Maintenance record not found")
    return maintenance

@router.get("/maintenance/", response_model=list[MaintenanceResponse])
def list_maintenance(db: Session = Depends(get_db)):
    return db.query(Maintenance).all()
