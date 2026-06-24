from sqlalchemy import Column, Integer, String
from database.database import Base


class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    plex_rating_key = Column(Integer, unique=True, index=True)

    title = Column(String)
    year = Column(Integer)

    sort_title = Column(String)
    studio = Column(String)
    content_rating = Column(String)

    duration = Column(Integer)