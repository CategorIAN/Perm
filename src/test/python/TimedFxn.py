from time import time

class TimedFxn:
    def __init__(self, function):
        self.function = function
        self.time = 0
        self.count = 0

    def __call__(self, *args, **kwargs):
        start = time()
        result = self.function(*args, **kwargs)
        functiontime = time() - start
        self.time += functiontime
        self.count += 1
        return result


  

