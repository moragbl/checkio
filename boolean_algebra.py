#!/usr/bin/python

OPERATION_NAMES = ("conjunction", "disjunction", "implication", "exclusive", "equivalence")

def boolean(x, y, operation):
    print "operation ", operation
    if operation == "conjunction":
        print "conjunciton ", " x is ", x, "y is ", y, " x and y is ", (x and y)
        return (x and y)
    elif operation == "disjunction":
        return (x or y)
    elif operation == "implication":
        return ((not x) or y)
    elif operation == "exclusive":
        return ( (x or y) and not(x and y))
    elif operation == "equivalence":
        return (not ((x or y) and not (x and y)))
    else:
        return 0

assert boolean(1, 0, "conjunction") == 0, "and"
assert boolean(1, 0, "disjunction") == 1, "or"
assert boolean(1, 1, "conjunction") == 1, "and"
assert boolean(1, 1, "implication") == 1, "material"
assert boolean(0, 1, "exclusive") == 1, "xor"
assert boolean(0, 1, "equivalence") == 0, "same?"
