import string
from collections import Counter

def main():
	# prompt user on desire to use a 'stopwords' file
    swPrompt = decisionPrompt('Would you like to use a Stop Words file? (y or n): ')
    
    # if stopword file is to be used, prompt for the filename
    if (swPrompt == 'Y' or swPrompt == 'y'):
    
        swFileName = input('Please enter the filename of the stopwords file: ')
        
        # open the stopwords file and store in memory for later use
        stStopWords = fileReader(swFileName, 's')
    
        # prompt for a dictionary filename
        wcFileName = input('Please enter the filename of the Word Count file: ')
        
        # open word count file and store in memory for later use
        lsWordCount = fileReader(wcFileName, 'l')
        
        dcWords = wordCounter(lsWordCount, swPrompt, stStopWords)
    elif (swPrompt == 'N' or swPrompt == 'n'):
    
        # prompt for a dictionary filename
        wcFileName = input('Please enter the filename of the Word Count file: ')
        
        # open word count file and store in memory for later use.
        # storing as list to get every instance of the word in the
        # file.
        lsWordCount = fileReader(wcFileName, 'l')
        
        dcWords = wordCounter(lsWordCount, swPrompt)
       
    
    sortedCount = Counter(dcWords).most_common(10)
    for items in sortedCount:
        print(str(items).strip('()'))
    

def decisionPrompt(input_string):
    while True:
        answer = input(input_string)
        if (answer == 'Y' or answer == 'y'
            or answer == 'N' or answer == 'n'):
            break
    return answer

def fileReader(filename, flag):
    # Function opens a file and reads the text, line by line, word by word.
    # It then returns the text as either a set or list (depending on the flag)
    # with each word as a value. This function expects that there are no newline
    # or carriage return symbols in the text file.
    
    try:
        F = open(filename, 'r')
    
    except IOError:
        print('Sorry, could not open file \'{}\''.format(filename))
        exit()

    else:
        if (flag == 's'):
            for line in F:
                readData = {word.strip(string.punctuation).lower()
                        for word in line.split()}
        elif (flag == 'l'):
            for line in F:
                readData = [word.strip(string.punctuation).lower()
                        for word in line.split()]
        F.close()
        return readData

def wordCounter(lsWordCount, swPrompt, *args):
    
    dcWordCount = {}
    for word in lsWordCount:
        if (swPrompt == 'N' or swPrompt == 'n'):
                dcWordCount.setdefault(word, 0)
                dcWordCount[word] += 1
                
        elif  (swPrompt == 'Y' or swPrompt == 'y'):
            if (word not in args[0]):
                dcWordCount.setdefault(word, 0)
                dcWordCount[word] += 1
                
    return dcWordCount
            

if __name__== '__main__':
    main()
