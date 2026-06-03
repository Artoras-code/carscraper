from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy import func
from app.database import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, nullable=False)
    email = Column(String, unique=True, index=True )
    hashed_password = Column(String, nullable=True)
    google_id = Column(String, unique=True, index=True )
    foto_perfil = Column(String, nullable=True)
    activo = Column(Boolean, default= True)
    created_at = Column(DateTime(timezone=True),server_default=func.now())

