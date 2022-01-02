import argparse
from datetime import datetime
from pathlib import Path

WORK_DIR = Path("./git-sandbox-submodule")

parser = argparse.ArgumentParser(description="Generate a text file")
parser.add_argument(dest="author", type=str, help="Creator of the text file")

args = parser.parse_args()


def run():
    time = datetime.now()
    with open(WORK_DIR / "data" / f"{time}.txt", "w") as f:
        f.write(f"Generated at {time} by {args.author}.")


if __name__ == "__main__":
    run()
