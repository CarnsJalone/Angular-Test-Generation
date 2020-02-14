from getConfigOption import getConfigurationOption

componentDecorator: str = getConfigurationOption('decorators', 'component')

def locateClass(pathToFile: str):
    with open(pathToFile) as component:
        lines: list[str] = component.read().split('\n')
        for line in lines:
            words: list[str] = line.split(' ')
            for word in words:
                if componentDecorator in word:
                    endChar: str = "})"
                    

locateClass('D:/Programming/Projects/BASF/FRONT_END/st-site/src/app/formula/paintline/slider-paintline.component.ts')