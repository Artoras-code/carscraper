from fastapi import FastAPI
from app.routes import vehiculos
from app.routes import auth

app = FastAPI(title="Carscraper")

app.include_router(vehiculos.router)
app.include_router(auth.router)

@app.get("/")
def root():
    return {"message": "CarScraper API funcionando"}