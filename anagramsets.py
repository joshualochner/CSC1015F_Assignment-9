from anagramsearch import isAnagram,strToDict

def getAllOccurences(listToCheck,item):
    toReturn = []
    
    for i in listToCheck:
        if(i[1]==item):
            toReturn.append(i[1])
            #listToCheck.remove(i)
            
    return toReturn

def main():
    fileName = 'EnglishWords.txt'
    #try:
    if(True):
        f = open(fileName)
        for line in f:
            if("START" in line):
                break
    
        linesToRead = f.readlines()
        f.close()
        
        listOfWords = {}

        wordLength = int(input('Enter word length:\n'))
        
        print('Searching...')
        for line in linesToRead:
            l = line.strip()
            if(len(l) == wordLength):
                listOfWords[l]=strToDict(l)

        finalList = []

        
        while (0<len(listOfWords)):
            listOfAnagrams = []
            firstVal = list(listOfWords.values())[0]
            for i in listOfWords:
                if(firstVal == listOfWords[i]):
                    listOfAnagrams.append(i)
            listOfAnagrams.sort()
            if(len(listOfAnagrams)>1):
                finalList.append(listOfAnagrams)
            for x in listOfAnagrams:
                del listOfWords[x]

        writeFileName = input('Enter file name:\n')
        w = open(writeFileName,'w')

        print('Writing results...')
        finalList.sort()
        for i in finalList:
            print(i,file=w)
            
        w.close()           

        
    #except:
        #pass
        
if __name__ == '__main__':
    main()