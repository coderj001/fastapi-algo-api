import asyncio
from typing import Tuple

from fastapi import FastAPI

from conf import settings


async def exec_bin(program: str = None, params: str = None) -> Tuple[str, str]:
    proc = await asyncio.create_subprocess_exec(
        settings.get("curdir") / "bin" / program,
        params,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    return (stdout.decode("utf-8"), stderr.decode("utf-8"))


def create_app() -> FastAPI:
    app = FastAPI()
    return app
