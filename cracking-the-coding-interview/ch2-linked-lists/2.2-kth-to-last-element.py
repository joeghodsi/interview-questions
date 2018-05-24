'''
Problem: find the kth to last element of a linked list
Solution: will assume k=1 means return the last element. use two pointers where p1 is k steps ahead
    of p2. iterate both pointers until p1 is null. return p2
    - linear time, constant space

total time: 20min

mistakes:
    - originally was off by one because while checked p1 not p1.next
'''
from setup import create_list_from_array


def kth_to_last(llist, k):
    p1 = p2 = llist

    if llist is None:
        raise Exception('list must be non-null')

    if k <= 0:
        raise Exception('k must be a whole number. received %d' % k)

    for i in xrange(k - 1):
        p1 = p1.next
        if p1 is None:
            raise Exception('k must not be greater than the length of the list. received %d' % k)

    while p1.next is not None:
        p1 = p1.next
        p2 = p2.next
    return p2

llist = create_list_from_array([1, 2, 3, 4, 5])
for i in xrange(1, 7):
    print kth_to_last(llist, i).data
print kth_to_last(llist, 0).data
print kth_to_last(None, 1)
