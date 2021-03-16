import sys
import os 
sys.path.append(os.path.abspath(os.path.join(__file__,"../../")))
from text_preprocessor.SentenceSplitter import SentenceSplitter
from decorator.WriteDecorator import WriteAfter
from decorator.ReadDecorator import ReadBefore
import argparse
import logging

logging.basicConfig(level=logging.INFO)

def parseArgs():
    parser=argparse.ArgumentParser()
    parser.add_argument('-f','--filename',default='datasets/bangla.txt',help='file name')
    args=parser.parse_args()
    return args.filename


@ReadBefore
@WriteAfter(filename="output/SplitedSentence.txt")
def main(filename: str, text : str = ""):
    ss=SentenceSplitter()
    textList=ss.split(text)
    return textList


if __name__=='__main__':
    filename=parseArgs()
    main(filename=filename)
    


