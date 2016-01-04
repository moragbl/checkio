#!/usr/bin/python

def count_inversion(sequence):
    """
        Count inversions in a sequence of numbers
    """
    number_list = list(sequence)
    inversions = 0
    while sorted(number_list) != number_list:
        for x in range (0,len(number_list)-1):
            if not (number_list[x] < number_list[x+1]):
                inversions +=1
                temp = number_list[x]
                number_list[x] = number_list[x+1]
                number_list[x+1] = temp
    return inversions

assert count_inversion((1, 2, 5, 3, 4, 7, 6)) == 3, "Example"
assert count_inversion((0, 1, 2, 3)) == 0, "Sorted"
assert count_inversion((99, -99)) == 1, "Two numbers"
assert count_inversion((5, 3, 2, 1, 0)) == 10, "Reversed"
