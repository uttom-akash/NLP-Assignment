from text_preprocessor.knowledge import bangla_chars
from decorator.WriteDecorator import WriteAfter
from decorator.ReadDecorator import ReadBefore

class WordTokenizer(object):
    def __init__(self):
        self.punctuations=["।", ",", ";", ":", "?", "!", "'", ".", "\"", "-",
                "[", "]", "{", "}", "(", ")", '–', "—", "―", "~"]

    def baseTokenize(self, text: str) -> list:
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
    
    @ReadBefore
    @WriteAfter("output/tokenizedWords.txt")
    def tokenizeFileText(self,filename : str ,text : str = "") -> list :
        return self.baseTokenize(text)

    @WriteAfter("output/tokenizedWords.txt")
    def tokenize(self, text: str) -> list:
        return self.baseTokenize(text)
