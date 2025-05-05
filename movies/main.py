from typing import Annotated

from fastapi import (
    FastAPI,
    Request,
    status,
    HTTPException,
    Depends,
)

from movies.schemas.movie import Movie

app = FastAPI(title="Movies catalog")

MOVIE_ITEMS = [
    Movie(
        movie_id=1,
        title="Белый лотос",
        description="Секс, интриги, убийство — в роскошном отеле. Один из лучших сериалов HBO последних лет",
        rating=7.6,
    ),
    Movie(
        movie_id=2,
        title="Пантеон",
        description="Мэдди пытается освободить сознание отца из цифрового рабства. Анимация о конфликте человека и его творения",
        rating=8.5,
    ),
]


@app.get("/")
def read_root(request: Request):
    docs_url = request.url.replace(path="/docs")
    return {
        "message": "Главная ведёт на страницу документации",
        "docs": str(docs_url),
    }


@app.get("/movies-list/", response_model=list[Movie])
def get_movies_list():
    return MOVIE_ITEMS


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


@app.get("/movies/{movie_id}", response_model=Movie)
def get_movie_details(movie_detail: Annotated[Movie, Depends(prefetch_movie)]):
    return movie_detail
