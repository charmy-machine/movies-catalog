from fastapi import (
    FastAPI,
    Request,
)

from api import router as api_router

app = FastAPI(title="Movies catalog")

app.include_router(api_router)


@app.get("/")
def read_root(request: Request):
    docs_url = request.url.replace(path="/docs")
    return {
        "message": "Docs url is...",
        "docs": str(docs_url),
    }
