'''
f = open("possible.py","r")
possibleList = []
allText = f.readlines()
for line in allText:
    line = line.split(" ")
    for item in line:
        try:
            if(item[-1]=='\n'):
                item = item[:-1]
        except:
            pass
        if(item!=' ' and item!=''):
            possibleList.append(item)
print possibleList
'''
'''
from reallPossible import possibleList
f = open("realPossibleDict.py","w")
wordToAppend = "possibleDict = {"
for item in possibleList:
    wordToAppend = wordToAppend + "'"+item+"':1,"
print wordToAppend
f.write(wordToAppend)
f.close()
'''
from realPossibleDict import possibleDict
print possibleDict.has_key("bhu")