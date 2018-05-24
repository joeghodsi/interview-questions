'''
Problem: write a program that solves the Towers of Hanoi. Given 3 towers (stacks) and n blocks of
    increasing size the problem starts with the blocks in ascending order on the left tower
    (smallest block on top, largest on bottom). Outcome should have the blocks also stacked in
    ascending order on the right tower. Rule: blocks can only stack on larger blocks
Solution:
    1. from the right, find the first block that can move right and move it right to closest stack
        that it can move to (a block on s1 may not stack on the top block of s2 so it would have to
        move to s3), repeat
    2. if no block can move right, change direction. from the left, find the first block that can
        move left and move it left to closest stack that it can move to, repeat.
    INCORRECT - didn't come up with a clear algo for this. book has a <10 line recursive solution
        but I don't fully understand

total time: w/o code - 20 min
'''
