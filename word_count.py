import string

def main():
	# prompt user on desire to use a 'stopwords' file
    swPrompt = decisionPrompt('Would you like to use a Stop Words file? (y or n): ')
    
    # if stopword file is to be used, prompt for the filename
    if (swPrompt == 'Y' or swPrompt == 'y'):
    
        #swFileName = input('Please enter the filename of the stopwords file: ')
        swFileName = 'stopwords'
        
        # open the stopwords file and store in memory for later use
        stStopWords = stFileReader(swFileName)
    
        # prompt for a dictionary filename
        #wcFileName = input('Please enter the filename of the Word Count file: ')
        wcFileName = '98-0_cleaned.txt'
        
        # open word count file and store in memory for later use
        lsWordCount = lsFileReader(wcFileName)
        
        dcWords = wordCounter(lsWordCount, swPrompt, stStopWords)
    elif (swPrompt == 'N' or swPrompt == 'n'):
    
        # prompt for a dictionary filename
        #wcFileName = input('Please enter the filename of the Word Count file: ')
        wcFileName = 'counttest'
        
        # open word count file and store in memory for later use
        lsWordCount = lsFileReader(wcFileName)
        
        dcWords = wordCounter(lsWordCount, swPrompt)
        
    dcWords = sorted(dcWords.values(), reverse=True)
        
    print(dcWords)
    

    

def decisionPrompt(input_string):
    while True:
        answer = input(input_string)
        if (answer == 'Y' or answer == 'y'
            or answer == 'N' or answer == 'n'):
            break
    return answer

def stFileReader(filename):
    # Function opens a file and reads the text, line by line, word by word.
    # It then returns the text as a set with each word as a value.
    # This function expects that there are no newline or carriage return
    # symbols in the text file.
    
    with open(filename, 'r') as F:
        for line in F:
          readSet = {word.strip(string.punctuation) for word in line.split()}
    return readSet
    
def lsFileReader(filename):
    # Function opens a file and reads the text, line by line, word by word.
    # Text is returned (in all lowercase) as a list with each word as a value.
    # This function expects that there are no newline or carriage return
    # symbols in the text file.
    
    with open(filename, 'r') as F:
        for line in F:
          readList = [word.strip(string.punctuation).lower() for word in line.split()]
    return readList

def wordCounter(lsWordCount, swPrompt, *args):
    
    dcWordCount = {}
    for word in lsWordCount:
        if (swPrompt == 'N' or swPrompt == 'n'):
            if (word not in dcWordCount):
                dcWordCount[word] = 1
            elif (word in dcWordCount):
                dcWordCount[word] = dcWordCount[word] + 1
                
        elif  (swPrompt == 'Y' or swPrompt == 'y'):
            if (word not in dcWordCount and word not in args[0]):
                dcWordCount[word] = 1
            elif (word in dcWordCount):
                dcWordCount[word] = dcWordCount[word] + 1
                
    return dcWordCount
            

if __name__== '__main__':
    main()

