import logging
from iio.FileIO import FileIO
from functools import wraps

def WriteAfter(filename : str = "Text.txt",mode='w'):
    def decorator(func):
        file=FileIO()

        def write(texts):
            if type(texts) is list:
                if len(texts)==0 or type(texts[0]) is str :
                    file.writeLines(filename=filename,lines=texts,mode=mode)
                else :
                    file.writeJson(filename=filename,text=texts,mode=mode)
            elif type(texts) is dict :
                file.writeJson(filename=filename,text=texts,mode=mode)
            else :
                file.write(filename=filename,text=texts,mode=mode)

        @wraps(func)    
        def decorated(*args,**kwargs):
            
            logging.debug("Start Write Decorator for {}.".format(func.__name__))
            texts = func(*args,**kwargs)
            write(texts)
            logging.debug("End Write Decorator for {}.".format(func.__name__))
            
            return texts
        
        return decorated

    return decorator