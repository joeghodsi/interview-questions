'''
Problem: write function that determines whether a string has all unique characters. Also, write a
    solution that requires no additional data structures
Solution:
    - set solution: store chars in set. if hit then char was already in string
        - linear time, linear space
    - sort solution: sort string. not unique if two adjacent chars are equal
        - nlogn time, constant space (assuming in-place sort)
'''


def has_unique_characters1(string):
    '''set solution. linear time and space'''
    if not isinstance(string, basestring):
        return None

    characters = set()
    for character in string:
        if character in characters:
            return False
        characters.add(character)
    return True


def has_unique_characters2(string):
    '''sort solution. nlogn time, constant space because python sort is in-place. If requirement is
    not to modify input, can copy prior to sort. in python doesn't seems easy to sort string
    in-place'''
    if not isinstance(string, basestring):
        return None

    string = sorted(string)
    previous_character = None
    for character in string:
        if previous_character == character:
            return False
        previous_character = character
    return True


print has_unique_characters1(None), has_unique_characters2(None)
print has_unique_characters1(12.2), has_unique_characters2(12.2)
print has_unique_characters1(''), has_unique_characters2('')
print has_unique_characters1('aa'), has_unique_characters2('aa')
print has_unique_characters1('aba'), has_unique_characters2('aba')
print has_unique_characters1('abc'), has_unique_characters2('abc')
print has_unique_characters1('1.2'), has_unique_characters2('1.2')
