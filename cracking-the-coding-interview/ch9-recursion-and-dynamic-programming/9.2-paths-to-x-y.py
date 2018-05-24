'''
Problem: Given an nxm matrix, compute the count of all possible paths from (0, 0) to (x, y) assuming
    you can only move right and down
Solution: recursive - each step recurse going right and going down

struggles:
    - looked up best way to init an nxm matrix
'''


def paths_to_x_y_count_recursive(matrix, x, y):
    # O(n^2)
    def _paths_to_x_y_count_recursive(matrix, x, y, i, j):
        if i == x and j == y:
            return 1
        if i == len(matrix[0]) or j == len(matrix):
            return 0
        count_right = _paths_to_x_y_count_recursive(matrix, x, y, i + 1, j)
        count_down = _paths_to_x_y_count_recursive(matrix, x, y, i, j + 1)
        return count_right + count_down

    return _paths_to_x_y_count_recursive(matrix, x, y, 0, 0)


def paths_to_x_y_count_dp(matrix, count_matrix, x, y):
    # O(n)
    if x == 0 and y == 0:
        return 1
    if x < 0 or y < 0:
        return 0
    count_left = count_matrix[y][x - 1]
    if count_left == 0:
        count_left = paths_to_x_y_count_dp(matrix, count_matrix, x - 1, y)
        count_matrix[y][x - 1] = count_left
    count_up = count_matrix[y - 1][x]
    if count_up == 0:
        count_up = paths_to_x_y_count_dp(matrix, count_matrix, x, y - 1)
        count_matrix[y - 1][x] = count_up
    return count_left + count_up


xy = (9, 19)
matrix = [[0 for j in xrange(xy[0] + 1)] for i in xrange(xy[1] + 1)]
print paths_to_x_y_count_recursive(matrix, *xy)
count_matrix = [[0 for j in xrange(xy[0] + 1)] for i in xrange(xy[1] + 1)]
print paths_to_x_y_count_dp(matrix, count_matrix, *xy)
