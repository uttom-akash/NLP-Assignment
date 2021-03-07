from text_preprocessor.knowledge import LanguageInfo
import re

class WordTokenizer(object):
    def __init__(self,lang='bn'):
        if lang == 'bn' :
            self.punctuations = LanguageInfo.punctuations
        else :
            self.punctuations = LanguageInfo.punctuations

    def tokenize(self, text: str) -> list:
        pattern="[।,;:?!'\.\\-\[\]\{\}\(\)–—―~]"
        text = re.sub(pattern," ",text)
        tokens = list(map(str.strip,text.split()))

        return tokens

    def tokenizeWithPunctuation(self, text: str) -> list:
        tokens = [i for i in text.split()]
        final_tokens = []

        for i in tokens:
            word = i.strip()
            if word[-1] in self.punctuations:
                a = word[:-1]
                b = word[-1]
                final_tokens.append(a)
                final_tokens.append(b)
            elif word[0] in self.punctuations:
                a = word[1:]
                b = word[0]
                final_tokens.append(a)
                final_tokens.append(b)
            else:
                final_tokens.append(word)

        return final_tokens
    

    def uniqueTokenize(self, text: str) -> list:
        return list(set(self.tokenize(text)))
    
    def uniqueTokenizeWithPunctuation(self, text: str) -> list:
        return list(set(self.tokenizeWithPunctuation(text)))
    


