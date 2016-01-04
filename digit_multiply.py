#!/usr/bin/python

def checkio(number):
    number_list = list(str(number))
    print "original number list is ", number_list
    while '0' in number_list: number_list.remove('0')
    print "amended number_list is ", number_list
    answer = 1 
    for thing in number_list:
        print "thing is ", thing
        print "first answer is ", answer
	answer = answer*int(thing)
        print "answer after multiplying thing is ", answer
    print answer
    return answer

assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1
