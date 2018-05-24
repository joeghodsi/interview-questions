'''
Problem: Given a set of coin denominations, find the minimum number of coins to make a certain
    amount of change
Solution: Started with recursive DP solution which technically seemed to work but was very expensive
    and ultimately has the same failure as the iterative solution I came up with after
    - Turns out that the greedy solution (the iterative solution at the bottom) isn't guaranteed to
        work for certain change and denominations :(
    - The proper solution is https://youtu.be/NJuKJ8sasGk

total time: 1hr15m
'''

DENOMINATIONS = [10, 5, 4, 1]
DENOM_TO_INDEX = {d: i for i, d in enumerate(DENOMINATIONS)}


def smallest_change_INCORRECT1(change):
    cache = [[0 for _ in xrange(len(DENOMINATIONS))] for _ in xrange(change + 1)]

    def _is_cached(change):
        change_cache = cache[change]
        for denom in change_cache:
            if denom != 0:
                return True
        return False

    def _smallest_change(change):
        for denom in DENOMINATIONS:
            leftover = change - denom
            if leftover > 0:
                if _is_cached(leftover):
                    cache[change] = list(cache[leftover])
                else:
                    possible_leftover_cache = list(_smallest_change(leftover))
                    if possible_leftover_cache is None:
                        continue
                    cache[change] = possible_leftover_cache
                cache[change][DENOM_TO_INDEX[denom]] += 1
                return cache[change]
            elif leftover == 0:
                cache[change][DENOM_TO_INDEX[denom]] += 1
                return cache[change]
        return

    return _smallest_change(change)


def smallest_change_INCORRECT2(change):
    smallest_change = [0 for _ in xrange(len(DENOMINATIONS))]
    for denom in DENOMINATIONS:
        count = change / denom
        if count >= 1:
            smallest_change[DENOM_TO_INDEX[denom]] = count
            change -= count*denom
    return smallest_change


x = 8
print smallest_change_INCORRECT1(x)  # correct answer is [0, 0, 2, 0]
print smallest_change_INCORRECT2(x)
print smallest_change_incomplete(x)
