'''
Problem: partition a linked list around a given pivot value, x, such that all nodes whose value is
    less than x come before all nodes that are greater than x
Solution: construct two lists (before and after) and iterate over the input list adding each node to
    the correct list. If a node exists with the pivot value, add it to a third list of pivot dups.
    Finally, merge before -> pivot -> after
    - linear time, constant space

total time: w/o code - 10 min
'''
