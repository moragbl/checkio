#!/usr/bin/python

def count_neighbours(grid, row, col):
    max_rows = len(grid)
    max_cols = len(grid[0])
    count = 0
    if not row == 0:
        count+=grid[row-1][col-1]
        if not col ==0:
            count+=grid[row-1][col]
    if not col == 0:
        count+=grid[row][col-1]
    if row < max_rows-1:
        count+=grid[row+1][col]
        if not col == 0:
            count+=grid[row+1][col-1]
    if col < max_cols-1:
        if not row == 0:
            count+=grid[row-1][col+1]
        count+=grid[row][col+1]
    if col < max_cols-1 and row < max_rows-1:
        count+=grid[row+1][col+1]
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

