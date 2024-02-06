import argparse
from pathlib import Path
import logging
from shutil import copyfile
from threading import Thread

parser = argparse.ArgumentParser(description="Sorting Folder")
parser.add_argument("--source", "-s", help="Source Folder", required=True)
parser.add_argument("--output", "-o", help="Output Folder", default="new_folder")

print(parser.parse_args())
args = vars(parser.parse_args())
print(args)

source = Path(args.get("source"))
output = Path(args.get("output"))

folders = []


def grabs_folder(path: Path):
    for element in path.iterdir():
        if element.is_dir():
            folders.append(element)
            grabs_folder(element)


def copy_file(path: Path):
    for element in path.iterdir():
        if element.is_file():
            ext = element.suffix[1:]
            ext_folder = output / ext
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)
                copy_file(element, ext_folder / element.name)
            except OSError as err:
                logging.error(err)


if __name__ == "main":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")
    folders.append(source)
    grabs_folder(source)
    print(folders)

    threads = []

    for folder in folders:
        th = Thread(target=copy_file, args=(folder,))
        th.start()
        threads.append(th)

    [th.join() for th in threads]
    print(f"can be deleted {source}")
