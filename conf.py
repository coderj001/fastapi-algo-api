from pathlib import Path

from pydantic import BaseSettings

curdir = Path(__file__).resolve().parent


class Settings(BaseSettings):
    secret_key: str = "dce9204c9d78f2de890dbf56b65a6578969fed40ecfacda77bd29bdc9ec0"
    debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    curdir: Path = curdir


settings = Settings().dict()
