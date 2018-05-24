'''
Problem: given two 32 bit integers, x and y, and two bit indicies, i and j, merge y into x between
    i and j. Example: x = 10000000, y = 1101, i = 1, j = 4; answer = 10011010
    - note: you can assume that you will always have enough space in x between i and j to fit y
'''


def merge_ints_by_bits(x, y, i, j):
    mask = -1
    for k in xrange(i, j + 1):
        mask = mask & ~(1 << k)

    x_cleared_i_to_j = x & mask
    y_shifted = y << i
    return x_cleared_i_to_j | y_shifted
