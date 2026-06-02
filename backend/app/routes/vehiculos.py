from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.database import get_db
from app.models.vehiculos import Vehiculo
from app.schemas.vehiculos import VehiculoCreate, VehiculoResponse

router = APIRouter(prefix="/vehiculos", tags=["Vehiculos"])

@router.get("/", response_model=List[VehiculoResponse])
def get_vehiculos(db: Session = Depends(get_db)):
    vehiculos = db.query(Vehiculo).all()
    return vehiculos

@router.get("/{vehiculo_id}", response_model=VehiculoResponse)
def get_vehiculos(vehiculo_id: int, db: Session = Depends(get_db)):
    vehiculo = db.query(vehiculo).filter(vehiculo.id == vehiculo_id).first()
    if not vehiculo:
        raise HTTPException(status_code=404, detail="No se escontrado lo que buscas")
    return vehiculo

@router.post("/", response_model=VehiculoResponse)
def create_vehiculo(vehiculo: VehiculoCreate, db: Session = Depends(get_db)):
    db_vehiculo = Vehiculo(**vehiculo.model_dump())
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

@router.delete("/{vehiculo_id}")
def delete_vehiculo(vehiculo_id: int, db: Session = Depends(get_db)):
    vehiculo = db.query(Vehiculo).filter(Vehiculo.id == vehiculo_id).first()
    if not vehiculo:
        raise HTTPException(status_code=404, detail="No se escontontro lo que Buscas")
    db.delete(vehiculo)
    db.commit()
    return{"message": "Se elimino el Vehiculo"}