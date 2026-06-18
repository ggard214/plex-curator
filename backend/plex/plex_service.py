from plexapi.server import PlexServer
from dotenv import load_dotenv
import os

load_dotenv()

PLEX_URL = os.getenv("PLEX_URL")
PLEX_TOKEN = os.getenv("PLEX_TOKEN")

def get_plex():
    return PlexServer(PLEX_URL, PLEX_TOKEN)


def get_movies():
    plex = get_plex()

    movies = plex.library.section("Movies")

    return [
        {
            "title": movie.title,
            "year": movie.year
        }
        for movie in movies.all()
    ]