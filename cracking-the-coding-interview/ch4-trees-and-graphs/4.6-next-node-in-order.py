'''
Problem: Given node N in a BST, find the "next" node (ie the next node in an in-order traversal).
    May assume each node has a pointer to it's parent
Solution: If we were performing in-order traversal, N would have been visited when it's left subtree
    bottomed out (ie after performing in-order traversal on the subtree with root N.left). Therefore
    the next in-order node is either from running in-order on N.right or first node up parent chain
    where ancestor.data > N.data
    - linear time, constant space

total time: 25 min
'''


def next_in_order_node(node):
    def _next_in_order_from_right():
        curr = node.right
        if curr is None:
            return None
        while curr.left:
            curr = curr.left
        return curr

    in_order_child = _next_in_order_from_right()
    if in_order_child:
        return in_order_child

    parent = node.parent
    while parent:
        if parent.data > node.data:
            return parent

    return None
