import re

class SentenceSplitter(object):
    def __init__(self,lang='bn'):
        if lang == 'bn' :
            self.splitPattern = re.compile(".*?[।?]") #  ।, ?
        else :
            self.splitPattern = re.compile(".*?[\.?!]") # ., ?, !

    def splitWithPunctuation(self,text : str) -> list :
        splittedList = self.splitPattern.split(text)
        splittedList = list(map(str.strip,splittedList))
        return splittedList
        
         
    def split(self,text : str) -> list :
        splittedList = self.splitPattern.findall(text)
        splittedList = list(map(str.strip,splittedList))
        return splittedList

    