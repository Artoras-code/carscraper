from fastapi import FastAPI
from app.routes import vehiculos

app = FastAPI(title="Carscraper")

app.include_router(vehiculos.router)

@app.get("/")
def root():
    return{"message": "CarScraper API funcionando"}