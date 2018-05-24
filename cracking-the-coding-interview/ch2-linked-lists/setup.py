'''
Chapter 2 is about linked lists and while python apparently has a 'llist' library, I felt it would
be most beneficial for study purposes to quickly define my own Node and a helper to construct a list
from an array.
'''


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        return

    def __repr__(self):
        node = self
        print_val = ''
        while node.next is not None:
            print_val += '%s -> ' % node.data
            node = node.next
        print_val += '%s' % node.data
        return print_val

    def get_node(self, data):
        node = self
        while node is not None:
            if node.data == data:
                return node
            node = node.next
        return None


def create_list_from_array(arr):
    head = Node(arr.pop(0))
    current = head
    for val in arr:
        current.next = Node(val)
        current = current.next
    return head
