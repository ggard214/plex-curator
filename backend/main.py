from fastapi import FastAPI
from plex.plex_service import get_movies
from database.database import Base, engine
from database.models import Movie
from services.import_service import import_movies

app = FastAPI(
    title="Plex Curator",
    version="0.1.0"
)

Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {
        "message": "Plex Curator is alive!"
    }

@app.get("/movies")
def movies():
    return get_movies()

@app.post("/import")
def import_library():
    return import_movies()