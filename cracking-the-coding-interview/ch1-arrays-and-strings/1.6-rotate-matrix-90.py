'''
Problem: given an nxn matrix, rotate it 90 degrees
Solution: recursive soln. iterate over row. each step swap 4 cells:
    (x,x+offset) -> (x+offset, n-x) -> (n-x, n-x-offset) -> (n-x-offset, x) -> (x, x+offset)
    once full row iteration, recurse given new start cell and n-- where start cell is (i+1, j+1)
    basically, each iteration we rotate for outter border then recurse with inner matrix (ie matrix
    inside that outter border). however, for space complexity we are iterating rather than recursing
    - linear time, constant space (quadratic if recursion)

total time: 1.5hrs - again, fail interview
    - probably would have taken 1hr in interview because no googling silly things, no distractions
    - need to remember to always draw general case first... I always try to just visualize and do a
        sloppy drawing and get caught... Would save 20-30 mins if I just take the time to draw nice
        example first

struggles:
    - too many distractions with merc and some with alice - need to find a way to isolate during
        mock interviews
    - bad with matrix manip Qs. Remember to ALWAYS draw general solution first to spot what index
        manip needs to happen
    - wanted to find a way to lookup in 2d array given tuple = (x, y) -> M[tuple]) rather than
        matrix[x][y] - wasted probably 10-15 mins
'''


def rotate_matrix_90(matrix, n):
    index_n = n - 1

    for row_start in xrange(index_n):
        for offset in xrange(row_start, index_n - row_start):
            _swap_cells_clockwise(matrix, row_start, offset, index_n)


def _swap_cells_clockwise(matrix, start, offset, index_n):
    top_slide_i, top_slide_j = start, start + offset
    right_slide_i, right_slide_j = start + offset, index_n - start
    bottom_slide_i, bottom_slide_j = index_n - start, index_n - start - offset
    left_slide_i, left_slide_j = index_n - start - offset, start

    temp_top = matrix[top_slide_i][top_slide_j]
    matrix[top_slide_i][top_slide_j] = matrix[left_slide_i][left_slide_j]
    matrix[left_slide_i][left_slide_j] = matrix[bottom_slide_i][bottom_slide_j]
    matrix[bottom_slide_i][bottom_slide_j] = matrix[right_slide_i][right_slide_j]
    matrix[right_slide_i][right_slide_j] = temp_top


matrix = [
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
]
rotate_matrix_90(matrix, 5)
for i in xrange(5):
    print matrix[i]

print
matrix = [
    [1, 1, 1, 1],
    [2, 2, 2, 2],
    [3, 3, 3, 3],
    [4, 4, 4, 4],
]
rotate_matrix_90(matrix, 4)
for i in xrange(4):
    print matrix[i]

print
matrix = [
    [1, 1],
    [2, 2],
]
rotate_matrix_90(matrix, 2)
for i in xrange(2):
    print matrix[i]

print
matrix = [
    [1]
]
rotate_matrix_90(matrix, 1)
for i in xrange(1):
    print matrix[i]
