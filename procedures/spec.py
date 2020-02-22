import os
import sys

GENERIC_SPEC_FILE_PATH: str = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates', 'generic.spec.ts')

def hasSpecFile(pathToComponentFile: str):
    directory: str = os.path.abspath(os.path.dirname(pathToComponentFile))
    for fileName in os.listdir(directory):
        return True if 'spec' in fileName else False

def generateSpecFile(pathToComponentFile: str, tsFileName: str, className: str):
    specFileName: str = tsFileName.replace('.ts', '.spec.ts')
    fullDirectory: str = os.path.dirname(os.path.abspath(pathToComponentFile))
    localDirectory: str = os.path.basename(fullDirectory) if os.path.isdir(fullDirectory) else None
    TARGET_SPEC_FILE_PATH: str = os.path.join(fullDirectory, specFileName)
    

    print(tsFileName)
    

    with open(GENERIC_SPEC_FILE_PATH) as inSpecFile:
        with open(TARGET_SPEC_FILE_PATH, 'w') as outSpecFile:
            
            imported: bool = False

            for index, line in enumerate(inSpecFile.readlines()):

                # Step 1 - Import the class
                if not 'import' in line and not imported:
                    line = "\nimport {" + className + "} from './" + tsFileName.replace('.ts', '') + "'\n\n"
                    outSpecFile.write(line)
                    imported = True
                    continue
                
                # Step 1 - Replace the class name in the first describe block
                if 'describe' in line:
                    words: list[str] = line.split("'")
                    for word in words:
                        if word == 'INSERT_CLASS':
                            words[words.index('INSERT_CLASS')] = f"'{className}'"
                            line = ''.join(words)
                            outSpecFile.write(line)
                            continue
                    continue

                if 'INSERT_CLASS' in line:
                   line = line.replace('INSERT_CLASS', className)
                   outSpecFile.write(line)
                   continue
                
                else:
                    outSpecFile.write(line)
    
  