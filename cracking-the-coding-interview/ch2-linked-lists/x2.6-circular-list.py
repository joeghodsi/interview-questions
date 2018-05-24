'''
Problem: determine if a linked list is a circular linked list and, if so, return the node at the
    start of the circular portion
Solution: keep track of visited nodes in a set. first hit is start of circular loop. if no hit and
    list has been traversed completely, return None since it is not circular.
    - note : if problem was just to determine if circular or not, then two pointers 1x and 2x speed
        would work in linear time and constant space
    - note 2: book has constant space solution that relies on a bit of math that works like note 1
    - linear time, linear space

total time: w/o code - 5 min
'''
