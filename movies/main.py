from fastapi import (
    FastAPI,
    Request,
)

app = FastAPI(title="Movies catalog")


@app.get("/")
def read_root(request: Request):
    docs_url = request.url.replace(path="/docs")

    return {
        "message": "Hello World",
        "docs": str(docs_url),
    }
