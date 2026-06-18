from fastapi import FastAPI
from plex.plex_service import get_movies

app = FastAPI(
    title="Plex Curator",
    version="0.1.0"
)

@app.get("/")
def root():
    return {
        "message": "Plex Curator is alive!"
    }

@app.get("/movies")
def movies():
    return get_movies()