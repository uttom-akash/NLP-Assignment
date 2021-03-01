from decorator.PathDecorator import PathMiddleware
import logging
import json

class FileIO(object):
    def __init__(self):
        pass

    @PathMiddleware("F:/NLP Assignment")
    def read(self,filename: str) -> str:
        text=""
        try:
            with open(filename,'r',encoding='utf-8') as fin :
                text = fin.read()
        except IOError :
            logging.error("ERROR : File Read Error")
        finally :
            logging.info("Read completed from {}.".format(filename))
            return text
    
    @PathMiddleware("F:/NLP Assignment")
    def readLines(self,filename: str) -> list:
        lines=[]
        try:
            with open(filename,'r',encoding='utf-8') as fin :
                lines = fin.readlines()
        except IOError :
            logging.error("ERROR : File Read Error")
        finally :
            logging.info("Read lines completed from {}.".format(filename))
            return lines
    
    @PathMiddleware("F:/NLP Assignment")
    def write(self,filename: str, text : str, mode : str = 'w'):
        try:
            with open(filename,mode,encoding='utf-8') as fout :
                fout.write(text)
        except IOError :
            logging.error("ERROR : File Write Error")
        finally :
            logging.info("Write completed into {}.".format(filename))
    
    @PathMiddleware("F:/NLP Assignment")
    def writeJson(self,filename: str, text : dict, mode : str = 'w'):
        try:
            with open(filename,mode,encoding='utf-8') as fout :
                json.dump(text,fout, ensure_ascii=False,indent=4)
        except IOError :
            logging.error("ERROR : File Write Error")
        finally :
            logging.info("Json write completed into {}.".format(filename))
    
    @PathMiddleware("F:/NLP Assignment")
    def writeLines(self,filename: str, lines : list, mode : str = 'w'):
        try:
            with open(filename,mode,encoding='utf-8') as fout :
                fout.write("\n".join(lines))
        except IOError :
            logging.error("ERROR : File Write Error")
        finally :
            logging.info("Write lines completed into {}.".format(filename))
    