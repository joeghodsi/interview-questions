'''
Problem: remove duplicates from a linked list. Follow up: what if you are not allowed a linear space
Solution: place values in a set and if set hit, remove node.
    - Follow up solution: how to solve with constant space? this is kind of a dumb question. the
        only real way is n^2 where for each node you run through the remaining list and remove dups
    - linear time, linear space

total time: 8min
'''
from setup import create_list_from_array


def remove_dups(llist):
    seen = set()
    previous = None
    while llist is not None:
        if llist.data in seen:
            previous.next = llist.next
        else:
            seen.add(llist.data)
            previous = llist
        llist = llist.next

llist = create_list_from_array([5, 2, 3, 1, 2, 2, 3, 1, 1, 1, 1, 6])
remove_dups(llist)
print llist

llist = create_list_from_array([1, 2, 3])
remove_dups(llist)
print llist

llist = create_list_from_array([1, 1])
remove_dups(llist)
print llist

llist = create_list_from_array([1])
remove_dups(llist)
print llist

llist = None
remove_dups(llist)
print llist
