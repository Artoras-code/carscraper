from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class VehiculoBase(BaseModel):
    marca: str
    model: str
    year : int
    precio : float
    kilometraje : Optional[int] = None
    transmision : Optional[str] = None
    descripcion : Optional[str] = None
    url_publicacion : Optional[str] = None
    fuente : Optional[str] = None
    disponible: Optional[bool] = True

class VehiculoCreate(VehiculoBase):
    pass

class VehiculoResponse(VehiculoBase):
    id: int
    create_at: datetime

    class Config:
        from_attributes = True