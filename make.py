import os

from conf import settings

for f in os.listdir(settings.get("curdir") / "program"):
    print(f"Generating: {f}")
    os.system(f"g++ program/{f} -o bin/{f[:-4]}")
    print("Done")
