# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    assert type(shift) == int, "Parameter shift is not of int type"
    assert shift >= 0 and shift < 26, "Parameter shift is not in the required range"
    dick={}
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    for i,letter in enumerate(upper):
        dick[letter] = upper[(i+shift)%26]
    for i,letter in enumerate(lower):
        dick[letter] = lower[(i+shift)%26]
    return dick
    
def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    newText=''
    for symbol in text:
        newText+=coder.get(symbol,symbol)
    return newText

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### HINT: This is a wrapper function.
    return applyCoder(text,buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """

#ia textul si imparte-l in cuvinte(cu semne de punctuatie)
#mergi prin cuvintele obitnute si elimina semnele
#mergi prin cuvinte si fa-le lower sau upper
#tine un max_cuvinte gasite
#mergi prin range(26)
#        mergi prin cuvinte si aplica shiftul
#        mergi prin noile cuvinte
#                cauta-le in wordList , pt fiecare gasit aduna la gasite cu 1
#        daca gasite > max_cuvinte schimba-l si retine si numarul din 1-26
#returneaza numarul coresp pt max_cuvinte
    accepted_letters = string.ascii_lowercase+string.ascii_uppercase
    clean_words=[]
    clean_word=''
    for symbol in text:
        if symbol in accepted_letters:
            clean_word+=symbol
            if symbol == text[-1]:
                clean_words.append(clean_word)
        else:
            if len(clean_word):
                clean_words.append(clean_word)
                clean_word=''
    max_words_found=0
    shift=0
    for i in range(26):
        nr_words=0
        for word in clean_words:
            potential_word = applyShift(word, i)
            if isWord(wordList, potential_word):
                nr_words+=1
        if nr_words > max_words_found:
            shift = i
            max_words_found = nr_words
    return shift


def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    cipher = getStoryString()
    #print '##############################'
    #print cipher
    #print '##############################'
    wordList = loadWords()
    bestShift = findBestShift(wordList, cipher)
    #plain=applyShift(cipher, bestShift)
    #print plain
    #print '##############################'
    return applyShift(cipher, bestShift)
    
    
    
#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
#    wordList = loadWords()
#    s = applyShift('Hello, world!', 8)
#    bestShift = findBestShift(wordList, s)
#    assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
     decryptStory()
#    print findBestShift(wordList,"Mergi la mare in weekend sau nu?Astept sa imi raspunzi, da?!!!")
