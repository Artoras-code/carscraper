from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from app.database import get_db
from app.models.usuario import Usuario
from app.schemas.usuario import UsuarioRegistro, UsuarioLogin, GoogleAuth, TokenResponse , UsuarioResponse
from app.core.security import hash_password, verify_password, create_access_token
from app.core.dependencies import get_current_user
from dotenv import load_dotenv
import os


load_dotenv()

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/registro", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
def registro(datos: UsuarioRegistro, db: Session = Depends(get_db)):
    if db.query(Usuario).filter(Usuario.email == datos.email).first():
        raise HTTPException(status_code=400, detail="Email ya registrado")
    
    usuario = Usuario(
        nombre=datos.nombre,
        email=datos.email,
        hashed_password=hash_password(datos.password)
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    token = create_access_token({"sub": str(usuario.id)})
    return {"access_token": token, "usuario": usuario}
    

@router.post("/login", response_model=TokenResponse)
def login(datos: UsuarioLogin, db: Session = Depends(get_db)):
    usuario = db.query(Usuario).filter(Usuario.email == datos.email).first()
    if not usuario or not usuario.hashed_password:
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    if not verify_password(datos.password, usuario.hashed_password):
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    token = create_access_token({"sub": str(usuario.id)})
    return {"access_token": token, "usuario": usuario}

@router.post("/google", response_model=TokenResponse)
def google_auth(datos: GoogleAuth, db: Session = Depends(get_db)):
    try:
        info = id_token.verify_oauth2_token(datos.token, google_requests.Request(), GOOGLE_CLIENT_ID)
    except Exception:
        raise HTTPException(status_code=401, detail="Token de Google inválido")
    
    email = info.get("email")
    google_id = info.get("sub")
    nombre = info.get("name", "")
    foto = info.get("picture")

    if usuario:
        if not usuario.google_id:
            usuario.google_id = google_id
            usuario.foto_perfil = foto
            db.commit()
    else:
        usuario = Usuario(
            nombre=nombre,
            email=email,
            google_id=google_id,
            foto_perfil=foto
        )
        db.add(usuario)
        db.commit()
        db.refresh(usuario)

    token = create_access_token({"sub": str(usuario.id)})
    return {"access_token": token, "usuario": usuario}

@router.get("/me", response_model=UsuarioResponse)
def mi_perfil(usuario: Usuario = Depends(get_current_user)):
    return usuario

            