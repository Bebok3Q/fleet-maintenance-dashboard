from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class VehicleBase(BaseModel):
    name: str
    vin: str
    mileage: float

class VehicleCreate(VehicleBase):
    pass

class VehicleResponse(VehicleBase):
    id: int

    class Config:
        from_attributes = True


class DiagnosticBase(BaseModel):
    error_code: str
    description: str

class DiagnosticCreate(DiagnosticBase):
    vehicle_id : int

class DiagnosticResponse(DiagnosticBase):
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True

class MaintenanceBase(BaseModel):
    service_type: str
    cost: float

class MaintenanceCreate(MaintenanceBase):
    vehicle_id: int

class MaintenanceResponse(MaintenanceBase):
    id: int
    service_date: datetime

    class Config:
        from_attributes = True