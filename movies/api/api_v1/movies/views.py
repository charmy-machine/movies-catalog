import random
from typing import Annotated
from annotated_types import Len

from fastapi import (
    Depends,
    APIRouter,
    Form,
    status,
)

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


@router.post(
    "/",
    response_model=Movie,
    status_code=status.HTTP_201_CREATED,
)
def create_movie(
    title: Annotated[str, Len(min_length=3, max_length=100), Form()],
    description: Annotated[str, Len(min_length=3, max_length=100), Form()],
):
    return Movie(
        movie_id=random.randint(1, 100),
        title=title,
        description=description,
        rating=round(random.uniform(8.0, 10.0), 2),
    )
