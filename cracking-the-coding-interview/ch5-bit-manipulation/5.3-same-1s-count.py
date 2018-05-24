'''
Problem: Given an integer return the next smallest and next largest integers that have the same
    number of 1 bits
Solution: count 1s in num. increment from num upward and count 1s for each int until first match.
    Do the same but decrement from num downward. Return both results
    - time: O(32/64 * (x + y)) where 32/64 depends on int size in OS, x is iterations through upward
        loop and y is iterations through downward loop. I consider _1s_count linear therefore total
        time complexity is on the order of O(n^2) assuming x and y are no more than 32/64 iterations
    - constant space

total time: 10 min
'''


def smaller_and_larger_with_same_1s(num):
    def _1s_count(n):
        mask = 1
        count = 0
        while mask > 0:
            if n & mask != 0:
                count += 1
            mask = mask << 1
        return count

    num_1s = _1s_count(num)
    next_greater = None
    next_smaller = None
    i = num
    while True:
        i += 1
        if _1s_count(i) == num_1s:
            next_greater = i
            break

    i = num
    while True:
        i -= 1
        if _1s_count(i) == num_1s:
            next_smaller = i
            break

    return next_greater, next_smaller
