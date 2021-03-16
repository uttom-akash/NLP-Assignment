class TableIO(object):
    def __init__(self,cellWidth : list , corner = "+",vertical= "|",horizontal="-"):
        self.cellWidth=cellWidth
        self.corner=corner
        self.vertical=vertical
        self.horizontal=horizontal
        self.save = False 
        self.formattedlines= []

        self.generateRowFormat()
    
    def setConfig(self,cellWidth : list , corner = "+",vertical= "|",horizontal="-"):
        self.cellWidth=cellWidth
        self.corner=corner
        self.vertical=vertical
        self.horizontal=horizontal

        self.generateRowFormat()
    
    def generateRowFormat(self):
        # {0 : <5}
        self.dataLine=" ".join(self.vertical+" {"+str(index)+": <"+str(self.cellWidth[index])+"}" for index in range(len(self.cellWidth)))+" "+self.vertical
        self.separatorLine = "+"+(sum(self.cellWidth)+3*len(self.cellWidth)-1)*"-"+"+"

    def printHeader(self,header=""):
        print()
        print(header)
        if self.save :
            self.formattedlines.append("")
            self.formattedlines.append(header)

    def printRow(self,data:list):
        line = self.dataLine.format(*data)
        print(line)
        if self.save :
            self.formattedlines.append(line)
    
    def printSeparator(self):
        print(self.separatorLine)
        if self.save :
            self.formattedlines.append(self.separatorLine)
