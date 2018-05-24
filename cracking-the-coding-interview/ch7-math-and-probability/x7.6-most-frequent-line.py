'''
Problem: given an array of 2D points, find the line that contains the most number of input points.
Solution: Define a line class with slope and y-intercept. Iterate over each point while iterating
    over the remaining points (ie i in xrange(len(points)) and j in xrange(i, len(points)))). For
    each new (a, b) generate the line and store it and a count in a map ({line, count}). Each time
    a line is seen again, increment the count. maintain a best_line var and at each iteration, check
    the current line count against the best_line count in the map and, if bigger, set current line
    as best_line.
    - O(n^2) time, O(n^2) space, where n is the number of input points
'''
