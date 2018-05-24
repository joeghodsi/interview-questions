'''
Problem: given a set, return all possible subsets
Solution: solution space size is sumation from 0 to n of the binomial coefficient (n i) where n is
    the size of the set - ie sum((n i)) for i = 0 .. n. Binomial coefficient is n!/i!(n - i)!. Book
    points out that this is the same as 2^n. Think of it like this: for each element, you choose
    whether it is in the subset or not (2 choices) so for n elements, each one has 2 choices, that's
    2*2*...*2 n times -> 2^n. That means that best case time and space are 2^n since each elem needs
    to choose.
    - As for the solution itself, subsets(s, i) = subsets(s, i - 1) + permutations(i elems from s).
    But, I think I can do this by looping over each element and creating new subsets by adding it to
    each subset in subsets and adding those new subsets to subsets
    - O(2^n) time and space

total time: 1hr20min :(
'''


def get_subsets(s):
    subsets = set()
    subsets.add(frozenset())  # empty set is subset of any set

    for value in s:
        current_subsets = subsets.copy()
        for subset in current_subsets:
            new_subset = set(subset)
            new_subset.add(value)
            subsets.add(frozenset(new_subset))

    return subsets


pick_count = 10
s = set(i for i in xrange(pick_count))
print s
subsets = get_subsets(s)
print subsets
print len(subsets)
