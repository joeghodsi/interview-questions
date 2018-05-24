'''
Problem: explain what the following does: ((n & (n - 1)) == 0)
Solution: n - 1 = n + (-1) and -1 is represented as all 1s. Adding any n to all 1s will flip all 0s
    until the rigth-most 1 and it will also flip the right-most 1 to 0. The only way x & y == 0 is
    if they are complements (ie 0011 and 1100) or if they are both zero. Since y in this case is
    x - 1, they can't both be zero. Also, since n - 1 leaves all bits to the left of the right-most
    1 intact, all left bits must be zero. Therefore this expression is checking whether n is a
    number with exactly one 1 bit AKA whether n is a power of two
    - linear time, linear space
'''
