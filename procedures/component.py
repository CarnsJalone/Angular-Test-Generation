
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


def getServices(pathToFile: str):

    CONSTRUCTOR_BEGIN: str = 'constructor('
    CONSTRUCTOR_END: str = ')'
    constructorBeginLine: int = None
    constructorEndLine: int = None

    with open(pathToFile) as component:
        lines: list[str] = component.readlines()
        injectables: list[str]
        addInjectors: bool = False

        for index, line in enumerate(lines):
            if CONSTRUCTOR_BEGIN in line:
                constructorBeginLine = index
            if constructorBeginLine and CONSTRUCTOR_END in line:
                constructorEndLine = index
                break
            
        injectables = lines[constructorBeginLine:constructorEndLine]
        for injectable in injectables:
            print(injectable)
        # print(injectables)
        

        # if constructorBeginLine and constructorBeginLine:
        #     print(lines[constructorBeginLine:contructorEndLine])
        