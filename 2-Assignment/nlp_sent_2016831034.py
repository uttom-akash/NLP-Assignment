import sys
import os 
sys.path.append(os.path.abspath(os.path.join(__file__,"../../")))
from text_preprocessor.SentenceSplitter import SentenceSplitter
import argparse
import logging

logging.basicConfig(level=logging.DEBUG)

def parseArgs():
    parser=argparse.ArgumentParser()
    parser.add_argument('-f','--filename',default='datasets/bangla.txt',help='file name')
    args=parser.parse_args()

    return args.filename

if __name__=='__main__':
    filename=parseArgs()
    ss=SentenceSplitter()
    ss.splitFileText(filename=filename)


