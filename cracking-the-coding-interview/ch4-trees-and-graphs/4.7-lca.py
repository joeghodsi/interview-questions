'''
Problem: given any two nodes in a binary tree, find their lowest common ancestor. Do not store nodes
    in a data structure
Solution: pre-order traversal keeping track of ancestors at each depth for both nodes. Once a node
    is found, no longer change its ancestor. If nodes are at different depths, as recursion bubbles
    up only the lower depth ancestor goes back up until they are at the same depth. Once both nodes
    are found, at each depth check if ancestors as equal. First time this is true, LCA found.
    - Note: this may work but the book does it very different and online sources match what the book
        does. Therefore I'm worried that this solution is buggy in some way
    - linear time, linear space

total time: 1hr
    - this took way too long. recurision is a big weak point for me.

mistakes:
    - didn't consider None input
struggles:
    - couldn't think of isinstance
    - slow to think of making nodes same depth and stepping together for LCA
'''


def lca(root, node1, node2):
    def _lca(node, node1, node2, ancestor_node1, ancestor_node2):
        # flag that the the node was found by marking it as None
        if node == node1:
            node1 = None
        if node == node2:
            node2 = None

        # if node has yet to be found, assign current node as ancestor
        if node1 is not None:
            ancestor_node1 = node
        if node2 is not None:
            ancestor_node2 = node

        if node is not None and (node1 is not None or node2 is not None):
            # not leaf node and both nodes have yet to be found
            left_result = _lca(node.left, node1, node2, ancestor_node1, ancestor_node2)
            right_result = _lca(node.right, node1, node2, ancestor_node1, ancestor_node2)

        if left_result is not None:
            return left_result
        if right_result is not None:
            return right_result

        if node1 is None and node2 is None and ancestor_node1 == ancestor_node2:  # LCA found!
            # both nodes have been found and first instance of ancestors being the same
            return ancestor_node1

    return _lca(root, node1, node2, root, root)
