#!/usr/bin/python

FIZZ = 3
BUZZ = 5

def fizzbuzz(number):
    print number
    if not (number%FIZZ or number%BUZZ):
        print "FizzBuzz"
    elif not (number%FIZZ):
        print "Fizz"
    elif not (number%BUZZ):
        print "Buzz"
    else:
        print "Not divisible by 3 or 5" 

number = raw_input("enter an integer please: ")
fizzbuzz(int(number))

