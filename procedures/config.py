import os
import sys
import json 

def openConfigFile() -> str:
    currentDirectory: str = os.path.dirname(os.path.abspath(__file__))
    parentDirectory: str = os.path.dirname(currentDirectory)
    with open(os.path.join(parentDirectory, 'config.json')) as infile:
        return infile.read()

def locateOption(file: str, type: str, key: str) -> str:
    config: dict = json.loads(file)[type]
    return config.get(key)

def getOption(optionType: str, optionValue: str):
    """
    Returns a configuration option from `config.json` \n
    `Parameter` (string) optionType - The type of option to search for \n
    `Parameter` (string) optionValue - The value of the option to search for \n 
    `Returns` (string) Configuration option \n
    `Example` - getOption('fileOptions', 'rootDir') -> returns the root directory specified in config.json
    """
    config: str = openConfigFile()
    return locateOption(config, optionType, optionValue)



