import os
import shutil
from subprocess import PIPE
from pathlib import Path
import hashlib

def duplicateFiltering(file):
    hasher = hashlib.sha256()
    with open(file, 'rb') as f:
        while True:
            chunk = f.read(8192)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()


def getDownloadsFolder():
    return Path.home() / "Downloads"

def createNewFolder(parentFolder, name: str):
    return parentFolder / name
    

def main():
    downloadsFolder = getDownloadsFolder()
    createNewFolder(downloadsFolder, 'Images')
    for item in downloadsFolder.iterdir():
        pass

if __name__ == "__main__":
    main()