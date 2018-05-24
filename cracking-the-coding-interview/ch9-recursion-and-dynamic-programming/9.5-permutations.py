'''
Problem: Return all permutations of a given string
Solution: Iterate over the elements and lock the current elem in as the ith elem in a partial
    permutation then recurse with the remaining values sans the ith element. Eventually there will
    be no more remaining values and you will have a single complete permutation. When the entire
    call is complete, it will have made all permutations. While I'm storing the perms outside the
    function to limit memory usage, this is not a DP solution as it isn't relying on the previous
    results
    - O(n!) time and space

total time: 45mins :)
'''


_permutations = []


def all_permutations(string):
    def _fill_permutations(partial_permutation, remaining_characters):
        if len(remaining_characters) == 0:
            _permutations.append(partial_permutation)
            return
        for index, value in enumerate(remaining_characters):
            new_partial_permutation = partial_permutation + value
            new_remaining_values = remaining_characters[:index] + remaining_characters[index + 1:]
            _fill_permutations(new_partial_permutation, new_remaining_values)

    _fill_permutations('', string)
    return set(_permutations)


string = 'abc'
permutations = all_permutations(string)
print permutations
print len(permutations)
