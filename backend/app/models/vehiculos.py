from sqlalchemy import Column, Integer, String, Float, DateTime, Boolean
from sqlalchemy.sql import func
from app.database import Base

class Vehiculo(Base):
    __tablename__ = "vehiculos"

    id = Column(Integer, primary_key=True, index=True)
    marca = Column(String, nullable=False)
    modelo = Column(String, nullable=False)
    year = Column(Integer, nullable=False)
    precio = Column(Float, nullable=False)
    kilometraje = Column(Integer)
    transmicion = Column(String)
    descripcion = Column(String)
    url_publicacion = Column(String)
    fuente = Column(String)
    created_at = Column(DateTime, server_default=func.now)
    disponible = Column(Boolean, default=True)
