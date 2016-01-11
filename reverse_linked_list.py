'''
Problem description:
Write a function that reverses a linked list
'''


class Node(object):
    def __init__(self, value=None):
        self.value = value
        self.next = None


def reverse_linked_list(head):
    '''
    runtime: O(n)
    space  : O(1)
    '''
    prev = None
    curr = head

    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next

    return prev
