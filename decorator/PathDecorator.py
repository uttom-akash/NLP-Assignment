import logging
from functools import wraps 

def PathMiddleware(root="F:/NLP Assignment"):
    def decorator(func):
        @wraps(func)
        def decorated(*args,**kwargs):
            
            logging.debug("Start Path Decorator for {}.".format(func.__name__))
            if 'filename' in kwargs :
                kwargs['filename']=root+"/"+kwargs['filename']
            f = func(*args,**kwargs)
            logging.debug("End Path Decorator for {}.".format(func.__name__))
            
            return f

        return decorated

    return decorator