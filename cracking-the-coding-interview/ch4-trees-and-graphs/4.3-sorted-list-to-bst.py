'''
Problem: Given a sorted array, return a BST with minimal height
Solution: BST requires all left nodes to be less than root and all right nodes to be greater than
    root. Root is middle elem of array. left is 1/4 elem of array. right is 3/4 elemn of array...
    - linear time, linear space

total time: 25 min

mistakes:
    - forgot BST definition... Thought it was lnode < root < rnode when it's really all nodes in
        left subtree < root < all nodes in right subtree that took 25 mins of my time...
    - thought midpoint was (end - start)/2 when it's really start + (end - start)/2 =>
        (start + end)/2
struggles:
    - couldn't think of isinstance
    - slow to think of making nodes same depth and stepping together for LCA
'''
from setup import Node


def BST_from_list(arr):
    def _BST_from_list(start, end, root=None):
        if end < start:
            return
        midpoint = int((end + start)/2)
        root = Node(arr[midpoint])
        _BST_from_list(0, midpoint-1, root.left)
        _BST_from_list(midpoint+1, end, root.right)
        return root

    if not len(arr):
        return None
    return _BST_from_list(0, len(arr) - 1)
