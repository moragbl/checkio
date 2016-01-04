#!/usr/bin/python

def checkio(words_set):
    if (len(words_set) <2 or len(words_set) > 29):
	return False
    for word1 in words_set:
        for word2 in words_set:
	    if word1.endswith(word2):
                if word1 != word2:
                    return True
    return False

assert checkio({"hello", "lo", "he"}) == True, "helLO"
assert checkio({"hello", "la", "hellow", "cow"}) == False, "hellow la cow"
assert checkio({"walk", "duckwalk"}) == True, "duck to walk"
assert checkio({"one"}) == False, "Only One"
assert checkio({"helicopter", "li", "he"}) == False, "Only end"
