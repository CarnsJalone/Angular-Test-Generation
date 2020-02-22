class ClassNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)


class FilenameNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)

class RootDirectoryNotFoundException(Exception):
    def __init__(self, message):
        super().__init__(message)