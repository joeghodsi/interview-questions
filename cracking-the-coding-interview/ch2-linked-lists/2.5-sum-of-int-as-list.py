'''
Problem: given two integers represented as linked lists where each node contains a single digit and
    the digits are stored in reverse order (ie 627 = 7 -> 2 -> 6), return the sum of the two numbers
Solution: solution is to step both lists at the same time and (1) sum the two digits (2) if greater
    than 10, flag a +1 for next step (3) sum % 10 is digit to store. Note: if one of the lists is
    longer than the other, when you reach the end of the other list, use 0 in sum
    - linear time, linear space (optimal since have to store solution somewhere...)

total time: w/o code - 10 min, code - 10 min; total - 20 min

mistakes:
    - didn't consider case when finished both lists and there is a carry_over in the final sum.
        should have final if outside the loop that checks carry_over and adds a Node(1) to end
'''
from setup import create_list_from_array, Node


def sum_ints_as_lists(int1, int2):
    if int1 is None:
        return int2
    if int2 is None:
        return int1

    carry_over = 0
    sum_head = sum_curr = None

    while int1 or int2:
        int1_data = int1.data if int1 else 0
        int2_data = int2.data if int2 else 0
        step_sum = int1_data + int2_data + carry_over
        carry_over = 1 if step_sum > 10 else 0
        step_digit = step_sum % 10

        if sum_curr is None:
            sum_head = sum_curr = Node(step_digit)
        else:
            sum_curr.next = Node(step_digit)
            sum_curr = sum_curr.next

        int1 = int1.next if int1 else None
        int2 = int2.next if int2 else None

    return sum_head

int1 = create_list_from_array([7, 2, 6])  # 627
int2 = create_list_from_array([8, 9, 1, 1])  # 1198
print sum_ints_as_lists(int1, int2)  # 1825 -> [5, 2, 8, 1]
