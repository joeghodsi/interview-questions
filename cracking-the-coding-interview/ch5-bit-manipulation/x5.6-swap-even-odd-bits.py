'''
Problem: Given an int, num, swap it's even bits with it's odd bits (ie swap bit 1 with bit 2, bit 3
    with bit 4, etc -> 0110 0010 becomes 1001 0001)
Solution: Brute force is to iterate in pairs and swap said pairs. This means you are performing
    32/64 swaps where you mask even and mask odd and shift them and set them in num. Instead,
    realize that you are continually swapping even bits with the bit to their right and odd bits
    with bits to their left. Therefore instead you could create a pair of masks (even mask:
    1010 1010, odd mask: 0101 0101) then AND both against the number to get the even bits (odd 0s)
    and odd bits (even 0s) then right-shift the even results and left-shift the odd results and OR
    them together
    - linear time, constant space
'''
