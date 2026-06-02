from fastapi import FastAPI

app = FastAPI(title="Carscraper")

@app.get("/")
def root():
    return{"message": "CarScraper API funcionando"}