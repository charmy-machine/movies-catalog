from pydantic import BaseModel


class MovieBase(BaseModel):
    movie_id: int
    title: str
    description: str
    rating: float


class Movie(MovieBase):
    """Movie model"""

    pass
