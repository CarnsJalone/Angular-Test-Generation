import os
import sys
import json 

def openConfigFile() -> str:
    currentDirectory: str = os.path.dirname(os.path.abspath(__file__))
    parentDirectory: str = os.path.dirname(currentDirectory)
    tokensDirectory: str = os.path.join(parentDirectory, 'config')
    with open(os.path.join(tokensDirectory, 'config.json')) as infile:
        return infile.read()

def locateOption(file: str, type: str, key: str) -> str:
    config: dict = json.loads(file)[type]
    return config.get(key)

def getConfigurationOption(type: str, key: str) -> str:
    config: str = openConfigFile()
    return locateOption(config, type, key)



