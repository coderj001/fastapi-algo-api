from pathlib import Path

from pydantic import BaseSettings

curdir = Path(__file__).resolve().parent

class Settings(BaseSettings):
    secret_key: str = ""
    debug: bool = True
    host: str = "localhost"
    port: int = 8000
    curdir: Path = curdir

settings = Settings().dict()
