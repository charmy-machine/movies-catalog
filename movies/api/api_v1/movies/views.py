from typing import Annotated

from fastapi import Depends, APIRouter

from api.api_v1.movies.crud import MOVIE_ITEMS
from api.api_v1.movies.dependencies import prefetch_movie
from schemas.movie import Movie

router = APIRouter(
    prefix="/movies",
    tags=["Movies"],
)


@router.get("-list/", response_model=list[Movie])
def get_movies_list():
    return MOVIE_ITEMS


@router.get("/{movie_id}", response_model=Movie)
def get_movie_details(movie_detail: Annotated[Movie, Depends(prefetch_movie)]):
    return movie_detail
