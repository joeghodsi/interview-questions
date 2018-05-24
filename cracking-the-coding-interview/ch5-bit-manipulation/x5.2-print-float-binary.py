'''
Problem: Given a real number between 0-1 (ex 0.72), print the binary representation. If the number
    cannot be represented accurately in binary with 32 characters, print 'error'
Solution: the 32 characters part is a hint. We know the number is less than one so the whole part
    will always be '0.'. The decimal portion can be treated as an integer for printing so start by
    determining decimal digits, multiply the number by decimal_count to get the whole number
    version (ex 72). At this point the problem devolves into 'print the binary representation of an
    integer' which is just looping 32/64 times (for 32/64 bit systems) right-shifting a mask
    (010...00 -> 0010...00) while ANDing the mask with your whole number representation.
    - linear time, linear space

total time: 10min w/o code
'''
