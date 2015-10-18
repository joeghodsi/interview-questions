'''
Problem description:
Given an array of unsorted integers, find the smallest positive integer not in the array.
'''


def find_smallest_missing_pos_int_sort(array):
    '''
    runtime: O(nlogn)
    space  : O(1) - this depends on the sort but python's list.sort() performs an in-place sort
    This sort-based solution is slow but requires no additional space, given the right sorting
    algorithm.
    '''
    array.sort()
    n = len(array)

    # move to index of first positive integer; if none exist, return 1
    index_of_first_pos = 0
    for index_of_first_pos in xrange(n):
        if array[index_of_first_pos] > 0:
            break

    current_pos_int = 1
    for i in xrange(index_of_first_pos, n):
        if array[i] != current_pos_int:
            return current_pos_int
        current_pos_int += 1

    return current_pos_int


def find_smallest_missing_pos_int_set(array):
    '''
    runtime: O(n)
    space  : O(n)
    This set-based solution is fast and readable but requires linear additional space.
    '''
    as_set = set(array)
    n = len(array)

    for x in xrange(1, n + 1):
        if x not in as_set:
            return x

    return n + 1


def find_smallest_missing_pos_int_optimal(array):
    '''
    runtime: O(n)
    space  : O(1)
    This in-place swap solution runs in linear time and requires constant space. Aside from some
    constant-factor performance optimizations, this is the optimal solution.
    '''
    n = len(array)

    def in_bounds(value):
        return 1 <= value <= n

    # swap integers within 1 to n into their respective cells
    # all other values (x < 1, x > n, and repeats) end up in the remaining empty cells
    for i in xrange(n):
        while in_bounds(array[i]) and array[i] != i + 1 and array[array[i] - 1] != array[i]:
            swap_cell = array[i] - 1
            array[i], array[swap_cell] = array[swap_cell], array[i]

    for i in xrange(n):
        if array[i] != i + 1:
            return i + 1

    return n + 1
