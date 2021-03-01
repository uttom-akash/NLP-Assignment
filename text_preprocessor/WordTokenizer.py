from text_preprocessor.knowledge import bangla_chars
from decorator.WriteDecorator import WriteAfter
from decorator.ReadDecorator import ReadBefore

class WordTokenizer(object):
    def __init__(self):
        self.punctuations=bangla_chars.punctuations

    def baseTokenizeWithPunctuation(self, text: str) -> list:
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
    
    def baseTokenize(self, text: str) -> list:
        tokens = [i for i in text.split()]
        final_tokens = []

        for i in tokens:
            word = i.strip()
            if word[-1] in self.punctuations:
                a = word[:-1]
                final_tokens.append(a)
            elif word[0] in self.punctuations:
                a = word[1:]
                final_tokens.append(a)
            else:
                final_tokens.append(word)

        return final_tokens
    
    @ReadBefore
    @WriteAfter("output/tokenizedWords.txt")
    def tokenizeFileTextWithPunctuation(self,filename : str ,text : str = "") -> list :
        return self.baseTokenizeWithPunctuation(text)

    @WriteAfter("output/tokenizedWords.txt")
    def tokenizeWithPunctuation(self, text: str) -> list:
        return self.baseTokenizeWithPunctuation(text)

    @ReadBefore
    @WriteAfter("output/tokenizedWords.txt")
    def tokenizeFileText(self,filename : str ,text : str = "") -> list :
        return self.baseTokenize(text)

    @WriteAfter("output/tokenizedWords.txt")
    def tokenize(self, text: str) -> list:
        return self.baseTokenize(text)

    @ReadBefore
    @WriteAfter("output/uniqueTokenizedWords.txt")
    def uniqueTokenizeFileText(self,filename : str ,text : str = "") -> list :
        return list(set(self.baseTokenize(text)))

    @WriteAfter("output/uniqueTokenizedWords.txt")
    def uniqueTokenize(self, text: str) -> list:
        return list(set(self.baseTokenize(text)))
    


