from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import get_db
from ..models import Diagnostic, Vehicle
from ..schemas import DiagnosticCreate, DiagnosticResponse

router = APIRouter()

@router.post("/diagnostics/", response_model=DiagnosticResponse)
def create_diagnostics(diagnostic: DiagnosticCreate, db: Session = Depends(get_db)):
    if not db.query(Vehicle).filter(Vehicle.id == diagnostic.vehicle_id).frist():
        raise HTTPException(status_code=404, detail="Vehicle not found")
    
    db_diagnostic = Diagnostic(**diagnostic.dict())
    db.add(db_diagnostic)
    db.commit()
    db.refresh(db_diagnostic)
    return db_diagnostic

@router.get("/diagnostics/{diagnostic_id}", response_model=DiagnosticResponse)
def get_diagnostic(diagnostic_id: int, db: Session = Depends(get_db)):
    diagnostic = db.query(Diagnostic).filter(Diagnostic.id == diagnostic_id).first()
    if not diagnostic:
        raise HTTPException(status_code=404, detail="Diagnostic not found")
    return diagnostic

@router.get("/diagnostics/", response_model=list[DiagnosticResponse])
def list_diagnostic(db: Session = Depends(get_db)):
    return db.query(Vehicle).all()
