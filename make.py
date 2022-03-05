import os

from conf import settings


def run_make():
    for f in os.listdir(settings.get("curdir") / "program"):
        print(f"Generating: {f}")
        exit_code = os.system(f"g++ program/{f} -o bin/{f[:-4]}")
        if exit_code == 0:
            print("Done")


if __name__ == "__main__":
    run_make()
