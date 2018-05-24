'''
Problem: Given two large trees, T1 (millions of nodes) and T2 (hundreds of nodes), determine if T2
    is a subtree of T1.
Solution: We are dealing with large trees here so space and time efficiency are key. We can break
    the problem into two parts:
        (1) tree equality: given two trees, determine if they are the same tree. This is a fairly
            straight forward problem that can't really be optimized beyond a standard tree traversal
            algorithm. Simply pre-order traverse both threes in tandem and check node equality at
            each step
        (2) run (1) the fewest number of times using the least space: this is the crux of this
            problem. You could simply run through T1 and, each time we hit a node that has the same
            data as T2.root, run (1) but that would be inefficient since for each such node we would
            run (1). Instead we could collect all nodes that match T2.root and customize (1) to
            operate on n trees rather than just two. That way we could check for equality all at
            once and each time we determine a tree isn't equal, we clear it in our list
    - linear time O(N + M) -> O(N), linear space O(N) worst case - given N elems in T1 and M in T2
        - note: space complexity would be a lot less in avg since we would only be storing the nodes
            from T1 that match the root of T2

total time: 20 min w/o code
'''
