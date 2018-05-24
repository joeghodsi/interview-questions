'''
Problem: Determine whether two strings are rotations of each other. Assume you are given an
    is_substring function that you may use only once.
Solution: iterate over str2 looking for first char of str1. If found iterate over str1 while
    incrementing an offset for str2 checking if the substr from str1 matches the start of str2.
    If it does and end of string is hit, check if first part of str1 matches second part of str2,
    otherwise, return False.
    - ended up not needing is_substring for my solution because I basically find the xy split of
        the strings and check for str1=xy, str2=yx, that str1.x == str2.x and str1.y == str2.y
    - solution in book is dumb... you have to have the clever thought that str2 is rotation of str1
        iff str2 in str1str1 (ie str1 cat with itself) which isn't intuitive. besides, I got the
        same time and space complexity... only thing book has is succinctness
    - linear time, constant space

total time: 30m*
    - realized after that my solution had bugs... they took up a bunch of extra time

struggles:
    - off-by-one type struggles
'''


def is_string_rotation(str1, str2):
    str1_len = len(str1)
    str2_len = len(str2)

    if str1_len != str2_len:
        return False

    i = 0
    while i < str2_len:
        if str2[i] == str1[0]:
            k = 1
            for j in xrange(1, str1_len):
                if i + k >= str2_len:
                    # if EOS and matching from str2[i] to str2[i + k] for str1[0] to str1[j] then
                    # is rotation if first part of str2 is second part of str1
                    return str2[:i] == str1[str1_len - i:]
                if str2[i + k] != str1[j]:
                    i += k
                    break
                k += 1
        else:
            i += 1
    return False

print is_string_rotation('abcd', 'cdab') == True
print is_string_rotation("I'm smart!", "mart!I'm s") == True
print is_string_rotation("I'm smart!", "art!I'm sm") == True
print is_string_rotation('water bottle', 'er bottlewat') == True
print is_string_rotation('abcd', 'abca') == False
print is_string_rotation('b', 'a') == False
print is_string_rotation('b', 'ab') == False
print is_string_rotation('ab', 'a') == False
