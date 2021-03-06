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
    if err:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"message": "Error with binary file.", "output": err},
        )
    return JSONResponse(status_code=status.HTTP_200_OK, content={"output": output})


@app.post("/palindrome_number_check")
async def palindrome_number_check_api(payload: PayLoad):
    output, err = await exec_bin(program="palindrome_number", params=payload.body)
    if err:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"message": "Error with binary file.", "output": err},
        )
    return JSONResponse(status_code=status.HTTP_200_OK, content={"output": output})


@app.post("/multiples_of_3_or_5")
async def multiples_of_3_or_5_api(payload: PayLoad):
    output, err = await exec_bin(program="multiples_of_3_or_5", params=payload.body)
    if err:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"message": "Error with binary file.", "output": err},
        )
    return JSONResponse(status_code=status.HTTP_200_OK, content={"output": output})

@app.post("/sum_square_diff")
async def sum_square_diff(payload: PayLoad):
    output, err = await exec_bin(program="sum_square_diff", params=payload.body)
    if err:
        return JSONResponse(
            status_code=status.HTTP_409_CONFLICT,
            content={"message": "Error with binary file.", "output": err},
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
