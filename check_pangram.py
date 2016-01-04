#!/usr/bin/python

def check_pangram(text):
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    present = False 
    for char in ALPHABET:
        if char in text.lower():
            present = True
        else:
            present = False
            break
    return present
    
    

assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
assert not check_pangram("ABCDEF"), "ABC"
assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"

