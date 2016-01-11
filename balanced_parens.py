'''
Problem description:
Given a string, determine whether or not the parentheses are balanced
'''


def balanced_parens(str):
    '''
    runtime: O(n)
    space  : O(1)
    '''
    if str is None:
        return True

    open_count = 0

    for char in str:
        if char == '(':
            open_count += 1
        elif char == ')':
            open_count -= 1
            if open_count < 0:
                return False

    return open_count == 0
