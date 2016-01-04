#!/usr/bin/python

def checkio(words):
    #split words on whitespace
    ThreeWords = False
    word_list = words.split()
    count = 0
    for word in word_list:
        if any(i.isdigit() for i in word):
            count = 0
        else:
            count +=1
    if count >= 3:
        ThreeWords = True
    return ThreeWords

#These "asserts" using only for self-checking and not necessary for auto-testing
assert checkio("Hello World hello") == True, "Hello"
assert checkio("He is 123 man") == False, "123 man"
assert checkio("1 2 3 4") == False, "Digits"
assert checkio("bla bla bla bla") == True, "Bla Bla"
assert checkio("Hi") == False, "Hi"
