import re
from decorator.WriteDecorator import WriteAfter
from decorator.ReadDecorator import ReadBefore
from text_preprocessor.knowledge.bangla_chars import punctuations

class SentenceSplitter(object):
    def __init__(self):
        self.splitPattern = re.compile(".*?[।?!]")

    def baseSplit(self,text : str) -> list :
        splittedList = self.splitPattern.findall(text)
        
        return splittedList
    
    @ReadBefore
    @WriteAfter(filename="output/SplitedSentence.txt")
    def splitFileText(self,filename : str ,text : str = "") -> list :
        return self.baseSplit(text)

    @WriteAfter(filename="output/SplitedSentence.txt")
    def splitText(self,text : str) -> list :
        return self.baseSplit(text)

    