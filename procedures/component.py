
def getClass(pathToFile: str):
    decoratorLine: int = None
    classFound: bool = False

    with open(pathToFile) as component:
        lines: list[str] = component.read().split('\n')
        for index, line in enumerate(lines):
            if '@Component' in line:
                decoratorLine = index
                break

        while not classFound:
            try:
                decoratorLine += 1
                if 'class' in lines[decoratorLine]:
                    classDeclarationLine: list[str] = lines[decoratorLine].split(' ')
                    return classDeclarationLine[classDeclarationLine.index('class') + 1]
            except:
                raise Exception("Unable to locate class")