'''
Problem: given nxm matrix, if a given cell is 0 then make all cells in row and column 0
Solution: two pass approach. maintain two bool arrays/bit vectors, one for rows and one for cols.
    traverse matrix and for each zero cell, mark the row and column in the respective bool arrays.
    second pass, if row or col in either bool array, mark cell as zero
    - linear time - O(n*m), O(n + m) space

total time: 13m
'''


def zero_cross(matrix, n, m):
    zero_rows = [False for i in xrange(n)]
    zero_cols = [False for i in xrange(m)]

    for i in xrange(n):
        for j in xrange(m):
            if matrix[i][j] == 0:
                zero_rows[i] = True
                zero_cols[j] = True

    for i in xrange(n):
        for j in xrange(m):
            if zero_rows[i] or zero_cols[j]:
                matrix[i][j] = 0


matrix = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 0, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 0, 4, 5],
]
zero_cross(matrix, 7, 5)
for i in xrange(7):
    print matrix[i]

print
matrix = [
    [1, 1, 1, 1],
    [2, 0, 0, 2],
    [3, 3, 3, 3],
]
zero_cross(matrix, 3, 4)
for i in xrange(3):
    print matrix[i]

print
matrix = [
    [0],
    [2],
]
zero_cross(matrix, 2, 1)
for i in xrange(2):
    print matrix[i]

print
matrix = [
    [1]
]
zero_cross(matrix, 1, 1)
for i in xrange(1):
    print matrix[i]
