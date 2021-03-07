from text_preprocessor.WordTokenizer import WordTokenizer
from text_preprocessor.SentenceSplitter import SentenceSplitter
import re
from collections import defaultdict

class Statistics(object):
    def __init__(self,lang='bn'):
        self.language=lang
    
    def generate(self,text : str ):
        stats=dict()
        stats['Corpus size (in words) excluding punctuation']=self.numberOfWords(text)
        stats['Corpus size (in chars) excluding spaces']=self.numberOfChars(text)
        stats['Average sentence length (in words)']=self.avarageSentenceLength(text)
        stats['Vocabulary size (no. of unique words)']= len(WordTokenizer().uniqueTokenize(text))
        stats['Corpus size (in lines)']=len(text.split('\n'))
        stats['Lexical diversity'] =self.safeDivision(stats['Vocabulary size (no. of unique words)'],stats['Corpus size (in words) excluding punctuation'])
        stats['Top ten frequent words']=self.topFrequentWords(text)
        
        return stats
        
    def safeDivision(self,nom,denom):
        return round(nom/denom,2) if denom!=0 else round(nom,2)

    def topFrequentWords(self,text:str,n=10):
        wt = WordTokenizer(lang=self.language)
        tokens = wt.tokenize(text)
        frequency=defaultdict(lambda:0)
        for token in tokens:
            frequency[token]+=1

        frequency ={k:v for k,v in sorted(frequency.items(), key=lambda item: -item[1])}
        tops=list()
        totalFreq=sum(frequency.values())
        for topK,topV in frequency.items():
            tops.append((topK,topV,self.safeDivision(topV,totalFreq)*100))
            n-=1
            if n==0 :
                break
        return tops
        
    def numberOfWords(self,text : str):
        wt = WordTokenizer(lang=self.language)
        tokens = wt.tokenize(text)
        return len(tokens)
    
    def numberOfChars(self,text:str):
        onlyText = re.sub("\s","",text)
        return len(onlyText)

    def avarageSentenceLength(self,text : str)-> list :
        splittedList = SentenceSplitter(lang=self.language).split(text)
        totalLength,numSentences= 0, len(splittedList)

        for sent in splittedList:
            totalLength+=len(sent.split())
        
        return self.safeDivision(totalLength,numSentences)