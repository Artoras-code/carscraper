from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class UsuarioRegistro(BaseModel):
    nombre: str
    email: EmailStr
    password: str

class UsuarioLogin(BaseModel):
    email: EmailStr
    password: str

class GoogleAuth(BaseModel):
    token: str

class UsuarioResponse(BaseModel):
    id: int
    nombre: str
    email: str
    foto_perfil: Optional[str]
    created_at: datetime

    class Config:
        from_attribute = True

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    usuario: UsuarioResponse