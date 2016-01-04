#!/usr/bin/python

def count_neighbours(grid, row, col):
    max_rows = len(grid)
    max_cols = len(grid[0])
    print "max_rows ", max_rows, "max_cols ", max_cols
    count = 0
    if row < max_rows-1:
        count+=grid[row+1][col-1]+grid[row+1][col]
        print "count a ", count
    if col < max_cols-1:
        count+=grid[row-1][col+1]+grid[row][col+1]
        print "count b ", count
    if (col < max_cols-1) and (row < max_rows-1):
        count +=grid[row+1][col+1]
        print "count c ", count
    count  += grid[row-1][col-1]+grid[row-1][col]+grid[row][col-1]
    print "count d ", count
    return count
if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 1, 2) == 3, "1st example"
    assert count_neighbours(((1, 0, 0, 1, 0),
                             (0, 1, 0, 0, 0),
                             (0, 0, 1, 0, 1),
                             (1, 0, 0, 0, 0),
                             (0, 0, 1, 0, 0),), 0, 0) == 1, "2nd example"
    assert count_neighbours(((1, 1, 1),
                             (1, 1, 1),
                             (1, 1, 1),), 0, 2) == 3, "Dense corner"
    assert count_neighbours(((0, 0, 0),
                             (0, 1, 0),
                             (0, 0, 0),), 1, 1) == 0, "Single"

