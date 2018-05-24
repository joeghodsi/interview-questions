'''
Problem: how would you design a stack which has push, pop, min all with O(1)
Solution: linked list. maintain head and min pointers. on push, check and update min if necessary.
    pop is the challenge since if we pop min then we need to find the next min. doing so would take
    linear time unless we maintain a second data structure such as a min heap. even then,
    rebalancing the heap on push would take log(n) which doesn't need to effect push's O(1) because
    it could be done on a separate thread but if another call comes in during rebalancing, it would
    need to sleep which essentially makes all calls O(log(n))
    - alternative: instead of min heap, each node also has a pointer to sorted_next which means if
        we iterate from min we get the sorted order. problem is each push would include a linear
        search & insert of the new node in the sorted_next linkage.

    - book solution: both of my solutions suck. true sol'n is each node stores value and min at that
        point in the stack. give away is you can't do anything sorted in constant time

total time: 15 min
'''
