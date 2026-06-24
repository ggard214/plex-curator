from database.database import SessionLocal
from database.models import Movie
from plex.plex_service import get_plex


def import_movies():

    print("Starting Import...")

    plex = get_plex()
    movies = plex.library.section("Movies").all()

    db = SessionLocal()

    imported = 0
    skipped = 0

    try:

        for movie in movies:

            print(movie.title)

            existing_movie = db.query(Movie).filter(
                Movie.plex_rating_key == movie.ratingKey
            ).first()

            if existing_movie:
                skipped += 1
                continue

            new_movie = Movie(
                plex_rating_key=movie.ratingKey,
                title=movie.title,
                year=movie.year,
                sort_title=movie.titleSort,
                studio=movie.studio,
                content_rating=movie.contentRating,
                duration=movie.duration
            )

            db.add(new_movie)
            imported += 1

        db.commit()

        return {
            "imported": imported,
            "skipped" : skipped
        }

    finally:
        db.close()