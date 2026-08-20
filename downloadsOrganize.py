import os
import shutil
from subprocess import PIPE
from pathlib import Path
import hashlib

def duplicateFiltering(folder):
    hashing = hashlib.sha256(folder)
    with open(folder, 'rb') as f:
        hashing.update(chunk)


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