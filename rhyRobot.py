from pinyin import PinYin
from reallPossible import possibleList
class LoopMachine:
    def __init__(self,numOfLoops,maximumValue):
        self.loopIndex = []
        self.numOfLoops = numOfLoops
        self.maximumValue = maximumValue
        for i in range(numOfLoops):
            self.loopIndex.append(0)

    def incr(self):
        if(self.shouldStop() == False):
            return 
        self.loopIndex[0] += 1
        for i in range(self.numOfLoops):
            if(self.loopIndex[i] >= self.maximumValue):
                if(i == self.numOfLoops - 1):
                    print('error')
                    return
                self.loopIndex[i] = 0
                self.loopIndex[i+1] += 1
    
    def shouldStop(self):
        #True represent continue
        #false represent stop
        flag = True
        for item in self.loopIndex:
            if(item >= self.maximumValue):
                flag = False
        return flag

    def prt(self):
        for item in self.loopIndex:
            print item,
        print
    
    def getLoopIndex(self):
        return self.loopIndex

class rhyRobot:
    #if baidu doesnot work.Try use proxy.
    def __init__(self):
        self.pinYinRobot = PinYin()
        self.pinYinRobot.load_word()
        self.shengMu = ["b","p","m","f","d","t","n","l","g","k","h","j","q","x","zh","ch","sh","r","z","c","s","y","w"]
        self.zhengTi = ["zhi","chi","shi","ri","zi","ci","si","yu","ye","yue","yuan","yin","yun","ying"]
        print("pinYinRobot is loaded")
    
    def findRhyForWords(self,chinese):
        pinYinList = self.pinYinRobot.hanzi2pinyin(chinese)
        for singleWord in pinYinList:
            for zhengTi in self.zhengTi:
                if(singleWord == zhengTi):
                    print singleWord+" is whole,cant rhy"
                    return
        pinYinTuple = self.__findPinYinTuple(pinYinList)
        allPossibleWord = self.__findAllPosiblePinYin(pinYinTuple)
        print allPossibleWord

    def __getResultFromBaidu(self,allPossibleWord):
        pass

    def __getResultFromLocal(self,allPossibleWord):
        pass

    def __findAllPosiblePinYin(self,pinYinTuple):
        shengMuLen = len(self.shengMu)
        myLoopMachine = LoopMachine(len(pinYinTuple),shengMuLen)
        allPossibleWord = []
        while(myLoopMachine.shouldStop()):
            loopIndex = myLoopMachine.getLoopIndex()
            newWord = ''
            appendFlag = True
            for i in range(len(loopIndex)):
                wordToAppend = self.shengMu[loopIndex[i]] + pinYinTuple[i][1]
                appendFlag = False
                for item in possibleList:
                    if(item == wordToAppend):
                        appendFlag = True
                if(appendFlag == False):
                    break
                newWord = newWord + wordToAppend + ' '
            if(appendFlag == True):
                allPossibleWord.append((newWord,0))
            myLoopMachine.incr()
        return allPossibleWord

    def __findPinYinTuple(self,pinYinList):
        pinYinTuple = []
        for item in pinYinList:
            if(item[:2] == "zh" or item[:2] == "ch" or item[:2]=="sh"):
                pinYinTuple.append((item[:2],item[2:]))
            else:
                pinYinTuple.append((item[:1],item[1:]))
        return pinYinTuple
m_rhyRobot = rhyRobot()
m_rhyRobot.findRhyForWords("五线谱")
''' 
#code to test LoopMachine
lm = LoopMachine(2,23)
for i in range(1000):
    lm.prt()
    lm.incr()
'''