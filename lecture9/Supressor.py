class Supressor:
    def __init__(self, exception):
        self.exception = exception

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        if type == self.exception:
            print("IndexError has been handled")
            return True
        return False
