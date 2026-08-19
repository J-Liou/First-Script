import os
import shutil
from subprocess import PIPE
from pathlib import Path

def duplicateFiltering():
    pass

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