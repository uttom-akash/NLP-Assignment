import re

class SentenceSplitter(object):
    def __init__(self,lang='bn'):
        if lang == 'bn' :
            self.splitPattern = re.compile(".*?[।?]") #  ।, ?
        else :
            self.splitPattern = re.compile(".*?[।?!]") # ।, ?, !

    def splitWithPunctuation(self,text : str) -> list :
        splittedList = self.splitPattern.split(text)
        return splittedList
        
         
    def split(self,text : str) -> list :
        splittedList = self.splitPattern.findall(text)
        return splittedList

    