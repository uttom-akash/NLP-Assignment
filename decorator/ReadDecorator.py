from iio.FileIO  import FileIO
import logging
from functools import wraps

def ReadBefore(func):
    def read(filename):
        file=FileIO()
        return file.read(filename=filename)
    
    @wraps(func)    
    def decorated(*args,**kwargs):
        
        logging.debug("Start Read Decorator for {}.".format(func.__name__))
        text=read(kwargs['filename'])
        kwargs['text']=text
        f = func(*args,**kwargs)
        logging.debug("End Read Decorator for {}.".format(func.__name__))
        
        return f 
    
    return decorated