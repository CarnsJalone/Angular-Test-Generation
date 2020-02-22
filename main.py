import sys
import argparse
from procedures.file import getFilePath
from procedures.component import getClass, getServices
from procedures.spec import hasSpecFile, generateSpecFile
from procedures.config import getOption

from exceptions.notFound import FilenameNotFoundException, RootDirectoryNotFoundException

filePath: str
className: str
hasSpec: bool

parser: argparse.ArgumentParser = argparse.ArgumentParser(description='Angular Test Generator')
parser.add_argument('--fileName', metavar='FN', type=str, help='Name of the file')
parser.add_argument('--rootDir', metavar='RD', type=str, help='Name of the root directory')
args = parser.parse_args()

rootDirectory: str
try:
    rootDirectory = args.rootDir
    if rootDirectory is None:
        rootDirectory = getOption('fileOptions', 'rootDir')
        if rootDirectory is None:
            raise FilenameNotFoundException('Unable to parse root directory. Please ensure it is specified as a command line argument or in config.json')
except Exception as e:
    print(e)


fileName: str
try:
    fileName = args.fileName
    if fileName is None:
        fileName = getOption('fileOptions', 'targetFileName')
        if fileName is None:
            raise FilenameNotFoundException('Unable to parse target file name. Please ensure it is specified as a command line argument or in config.json')
except Exception as e:
    print(e)

if fileName and rootDirectory:
    filePath = getFilePath(rootDir=rootDirectory, targetFileName=fileName)
    print(getServices(filePath))
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