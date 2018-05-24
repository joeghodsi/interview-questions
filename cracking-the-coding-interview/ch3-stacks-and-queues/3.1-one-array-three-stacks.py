'''
Problem: describe how you could use a single array to implement three stacks
Solution: assume static array. assume equal fixed space for each stack within array. maintain
    head and capacity border for each stack. each stack starts at the right end of their allocation
    and fill to the left until they hit their border
    - note: above solution is not smart about space and will likely be inefficient. we could design
        a dynamic stack space solution but it will have a worse time complexity because there would
        be a lot of data shifting each time values are inserted

total time: 10 min
'''
