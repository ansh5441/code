import pylab

# You may have to change this path
WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of uppercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def plotVowelProportionHistogram(wordList, numBins=1000):
    """
    Plots a histogram of the proportion of vowels in each word in wordList
    using the specified number of bins in numBins
    """
    vowel = ['a','e','i','o','u']
    numVowel = []
    numChar = []
    i = 0
    prop = []
    for word in wordList:
        numChar.append(len(word))
        numVowel.append(0)
        for char in word:
            if char in vowel:
                numVowel[i] += 1
        prop.append(numVowel[i]/float(numChar[i]))
        i += 1
    print(sum(prop)/83667)
    pylab.figure(1)
    pylab.hist(prop,bins = numBins)
    pylab.show()
                
    
    

if __name__ == '__main__':
    wordList = loadWords()
    plotVowelProportionHistogram(wordList)
