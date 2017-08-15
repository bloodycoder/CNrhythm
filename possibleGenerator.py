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
from reallPossible import possibleList
print possibleList
