import logging
from file_io.FileIO import FileIO
from functools import wraps

def WriteAfter(filename : str = "Text.txt"):
    def decorator(func):
        file=FileIO()

        def write(texts):
            if type(texts) is list :
                file.writeLines(filename=filename,lines=texts)
            else :
                file.write(filename=filename,text=texts)

        @wraps(func)    
        def decorated(*args,**kwargs):
            
            logging.debug("Start Write Decorator for {}.".format(func.__name__))
            texts = func(*args,**kwargs)
            write(texts)
            logging.debug("End Write Decorator for {}.".format(func.__name__))
            
            return texts
        
        return decorated

    return decorator