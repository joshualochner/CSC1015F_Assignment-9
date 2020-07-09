def strToDict(word):
    d = {}
    for i in word:
        if(i in d):
            d[i]+=1
        else:
            d[i]=1    
    return d

def isAnagram(word1,word2):
    return strToDict(word1) == strToDict(word2)

def main():
    print('***** Anagram Finder *****')
    fileName = 'EnglishWords.txt'
    try:
        f = open(fileName)
        for line in f:
            if("START" in line):
                break
    
        wordToCheck = input('Enter a word:\n')
        
        listOfAnagrams = []
        for line in f:
            line = line.strip()
            if(isAnagram(wordToCheck.lower(),line) and wordToCheck.lower() != line):
                listOfAnagrams.append(line)
        
        listOfAnagrams.sort()
        if(listOfAnagrams):
            print(listOfAnagrams)
        else:
            print("Sorry, anagrams of '"+wordToCheck+"' could not be found.")
        f.close()
    except:
        print("Sorry, could not find file '"+fileName+"'.")    


if __name__ == '__main__':
    main()