'''
Problem: write a function that takes in a string and compresses it such that all repeating
    characters are represented by a count. Example: 'aaabbcccc' -> 'a3b2c4'. If the resulting string
    is longer than the original, return the original
Solution: construct compressed string from scratch. place new char and count repeating chars. when
    char changes, add count and new char to compressed string and repeat. finally, add last count
    after loop
    - linear time, linear space (could do constant space if any assumptions about possible chars
        such as alphabet, ASCII, UNICODE by just creating new array with double the cells as the
        possible chars - ex: array of 52 if chars are guarenteed to be english alphabet)

total time: 1hr - this took wayyyyyyyy too long and would have been a failed interview

mistakes:
    - didn't initially think to construct compressed string from scratch. Instead copied original
        and altered as I went which caused all sorts of indexing issues and I need to keep track of
        several additional variables. this also required weird string splicing
struggles:
    - didn't know python strings are immutable
    - not familiar enough with string splicing
'''


def compress_string(string):
    if not isinstance(string, basestring):
        return None  # in prod, I'd let this raise instead of fail silently and assume result
    if len(string) == 0:
        return string

    compressed = string[0]
    count = 1
    previous_char = None

    for i in xrange(len(string)):
        if string[i] == previous_char:
            count += 1
        elif previous_char is not None:
            compressed += str(count) + string[i]
            count = 1
        previous_char = string[i]
    compressed += str(count)

    if len(compressed) > len(string):
        return string
    return compressed

print compress_string('abbbccccaa')
print compress_string('abcc')
print compress_string('a')
print compress_string('aa')
print compress_string('a2')
print compress_string('')
print compress_string(None)
