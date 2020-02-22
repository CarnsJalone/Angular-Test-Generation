import os

def getFilePath(rootDir: str, targetFileName: str):
    for subDirectory, directory, files in os.walk(rootDir):
        for fileName in files:
            if 'component' in fileName:
                if targetFileName == fileName:
                    return subDirectory + os.sep + fileName
    raise FileNotFoundError('Unable to locate message. Please ensure the correct .ts file is passed into the argument parser.')
