import uvicorn
from fastapi import FastAPI

from conf import settings

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host=settings.get("host"),
        port=settings.get("port"),
        log_level="info",
    )
