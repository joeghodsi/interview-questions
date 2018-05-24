'''
Problem: Given a BST, return a list of linked lists where each linked list contains all the nodes
    at that depth. Ex: list[3] is a linked list containing all nodes at depth 3
Solution: depth first traversal keeping track of depth and appending the node to the respective
    linked list or creating new list if there isn't one
    - linear time, linear space (n for lists + logn for recursion)

total time: 20 min
'''


def BST_to_depth_lists(root):
    lists = []

    def _BST_to_depth_lists(node, depth):
        if node is None:
            return
        if len(lists) == depth:
            # current depth has no linked list yet
            lists.append(node)
        else:
            curr_node = lists[depth]
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = node

        _BST_to_depth_lists(node.left, depth + 1)
        _BST_to_depth_lists(node.right, depth + 1)

    _BST_to_depth_lists(root, 0)
    return lists
