'''
Problem: Given a binary tree, print all paths within the tree where the sum of the nodes' data is
    the same as a given sum. A path may start or end anywhere in the tree
Solution: I honestly couldn't think of a solution. I thought it would be a permutations problem but
    the books solution is simple tree traverse
    - book's solution: O(nlogn) time and space. pre-order traverse tree passing down depth and the
        path from the root to the current node. At each node loop over the path in reverse (ie from
        current node up to root) summing the path as you go. Each time the sum matches the given
        sum, print the path from i (where you up currently in the backtrack of the path) to where
        the current node is (ie from i to depth in the path array)
'''
