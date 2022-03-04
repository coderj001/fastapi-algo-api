from typing import Optional

import uvicorn
from fastapi import status
from pydantic import BaseModel
from starlette.responses import JSONResponse

from conf import settings
from utils import create_app, exec_bin

app = create_app()


class PayLoad(BaseModel):
    body: Optional[str] = None


@app.get("/")
async def root():
    return {"message": "Hello World!"}


@app.post("/nth_fibonacci_number")
async def nth_fibonacci_number_api(payload: PayLoad):
    output, err = await exec_bin(program="nth_fibonacci_number", params=payload.body)
    print(output, err)
    if err:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"message": "Error with binary file."},
        )
    return JSONResponse(status_code=status.HTTP_200_OK, content={"output": output})


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        reload=settings.get("debug"),
        host=settings.get("host"),
        port=settings.get("port"),
        log_level="info",
    )
