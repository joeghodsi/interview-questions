'''
Problem: delete a node from a linked list, given only access to said node.
    Example: 1 -> 2 -> 3 -> 4 -> 5. Given node 3, return nothing but list now looks like
        1 -> 2 -> 4 -> 5
Solution: tricky... who knows how many places point to the node to be deleted, D. my idea is not to
    actually delete the node. instead stuff it's contents with that of the next node.
    - concern: can't delete the the last node. If acceptable, set to a empty-flagged node
    - constant time, constant space


total time: 20min
'''
from setup import create_list_from_array


def delete_node(node):
    if node is None or node.next is None:
        return
    node.data = node.next.data
    node.next = node.next.next

llist = create_list_from_array([1, 2, 3, 4, 5])
delete_node(llist.get_node(3))
print llist
delete_node(llist.get_node(2))
print llist
delete_node(llist.get_node(1))
print llist

# can't work
delete_node(llist.get_node(5))
print llist
##
delete_node(llist.get_node(4))
print llist
