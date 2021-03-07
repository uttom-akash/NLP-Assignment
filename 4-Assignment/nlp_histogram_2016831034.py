import sys 
import os 
sys.path.append(os.path.abspath(os.path.join(__file__,"../../")))
from text_preprocessor.Statistics import Statistics
from decorator.WriteDecorator import WriteAfter
from decorator.ReadDecorator import ReadBefore
from file_io.TableIO import TableIO

import argparse
import logging

logging.basicConfig(level=logging.INFO)

def parseArgs():
    parser=argparse.ArgumentParser()
    parser.add_argument('-fB','--filenameB',default='datasets/bangla.txt',help='bangla file name')
    parser.add_argument('-fE','--filenameE',default='datasets/english.txt',help='english file name')
    args=parser.parse_args()

    return (args.filenameB,args.filenameE)

@ReadBefore
def generateStats(filename: str, lang="bn", text : str = ""):
    st=Statistics(lang=lang)
    stats=st.generate(text)
    return stats


@WriteAfter(filename="output/histogram.txt")
def writeToConsole(states : list):
    banglaStats = states[0]
    englishStats = states[1]
    
    
    tbIO=TableIO(cellWidth=[50,15,15])
    tbIO.save=True
    tbIO.printHeader("[ STATISTICS ]")
    tbIO.printSeparator()
    tbIO.printRow(["",banglaStats['Language'],englishStats['Language']])
    tbIO.printSeparator()
    for k,v in banglaStats['stats'].items():
        if type(v) is list:
            continue 
        tbIO.printRow([k,banglaStats['stats'][k],englishStats['stats'][k]])
        tbIO.printSeparator()

    tbIO.printHeader("[ FREQUENT WORDS LIST ]")
    tbIO.setConfig(cellWidth=[25,10,10,25,10,10])
    tbIO.printSeparator()
    tbIO.printRow(["","ENGLISH","","","BANGLA",""])
    tbIO.printSeparator()
    tbIO.printRow(["Word","Freq","%","Word","Freq","%"])
    tbIO.printSeparator()
    for index in range(10): 
        banglaWord=banglaStats['stats']['Top ten frequent words'][index]
        englishWord=englishStats['stats']['Top ten frequent words'][index]
        tbIO.printRow([englishWord[0],englishWord[1],englishWord[2],banglaWord[0],banglaWord[1],banglaWord[2]])
        # tbIO.printSeparator()
    tbIO.printSeparator()
    
    return tbIO.formattedlines

@WriteAfter(filename="output/histogram.json")
def main(filename1: str,filename2: str):
    stats=list()
    banglaStats = dict()
    banglaStats['Language'] ="Bangla"
    banglaStats['stats'] = generateStats(filename=filename1)
    stats.append(banglaStats)
    englishStats = dict()
    englishStats['Language'] ="English"
    englishStats['stats'] = generateStats(filename=filename2,lang='en')
    stats.append(englishStats)
    writeToConsole(stats)
    return stats


if __name__=='__main__':
    filenameB,filenameE=parseArgs()
    main(filename1=filenameB,filename2=filenameE)