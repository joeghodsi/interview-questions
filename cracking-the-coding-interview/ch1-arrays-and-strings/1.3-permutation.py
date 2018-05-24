'''
Problem: given an two strings, determine if one is a permutation of the other
Solution: sort and compare with early return if not same length strings
    - nlogn time, constant space (assuming in-place sort)

total time: 10 minutes
'''


def are_permutations(str1, str2):
    if str1 is None or str2 is None:
        return None
    if not isinstance(str1, basestring) or not isinstance(str2, basestring):
        return None
    if len(str1) != len(str2):
        return False

    str1 = sorted(str1)
    str2 = sorted(str2)

    return str1 == str2


print are_permutations('abcd', 'dabc')
print are_permutations('abcd', None)
print are_permutations(None, None)
print are_permutations(12.2, 'abc')
print are_permutations('', '')
print are_permutations('abc', 'abx')
