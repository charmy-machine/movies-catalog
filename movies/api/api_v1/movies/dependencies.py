from fastapi import HTTPException
from starlette import status

from api.api_v1.movies.crud import MOVIE_ITEMS
from schemas.movie import Movie


def prefetch_movie(movie_id: int) -> Movie:
    movie_detail: Movie | None = next(
        (item for item in MOVIE_ITEMS if item.movie_id == movie_id), None
    )

    if movie_detail:
        return movie_detail

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Movie with id {movie_id!r} not found",
    )
