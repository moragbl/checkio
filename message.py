#!/usr/bin/python

def find_message(text):
    """Find a secret message"""
    message =  (''.join(letter for letter in text if letter.isupper()))
    return message

assert find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO", "hello"
assert find_message("hello world!") == "", "Nothing"
assert find_message("HELLO WORLD!!!") == "HELLOWORLD", "Capitals"
