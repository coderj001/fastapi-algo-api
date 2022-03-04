import asyncio
from typing import Dict

from conf import settings


async def exec_bin() -> Dict[str, str]:
    proc = await asyncio.create_subprocess_exec(
        settings.get("curdir") / "bin" / "nth_fibonacci_number",
        "10",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE,
    )
    stdout, stderr = await proc.communicate()
    return {"stdout": stdout.decode("utf-8"), "stderr": stderr.decode("utf-8")}


asyncio.run(exec_bin())
