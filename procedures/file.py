import os

def getFilePath(rootDir: str, targetFile: str):
    for subDirectory, directory, files in os.walk(rootDir):
        for file in files:
            if 'component' in file:
                if targetFile == file:
                    return subDirectory + os.sep + file
    raise FileNotFoundError('Unable to locate message. Please ensure the correct .ts file is passed into the argument parser.')
