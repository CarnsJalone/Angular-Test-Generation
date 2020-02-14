import sys
import argparse
from procedures.file import getFilePath
from procedures.component import getClass
from procedures.spec import hasSpecFile, generateSpecFile

filePath: str
className: str
hasSpec: bool

parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Angular Test Generator')
parser.add_argument('--fileName', metavar='FN', type=str, help='Name of the file')
parser.add_argument('--rootDir', metavar='RD', type=str, help='Name of the root directory')

args = parser.parse_args()
fileName = args.fileName if args.fileName is not None else None
rootDirectory = args.rootDir if args.rootDir is not None else None

if fileName and rootDirectory:
    filePath = getFilePath(rootDir=rootDirectory, targetFile=fileName)
    if not hasSpecFile(filePath):
        generateSpecFile(pathToComponentFile=filePath, tsFileName=fileName, className=getClass(filePath))
else:
    raise ReferenceError('Unable to reference file without both parameters')


# Procedure 1
# Take a file name as an argument

# Walk through project directory to locate file
# Find class in file
# Determine if a spec file exists
# Generate one if not