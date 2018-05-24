'''
Problem: Given a staircase with n steps, compute the count of all possible ways you could reach the
    top assuming you can take either 1, 2, or 3 steps in one go
Solution: recursive solution - each step recurse with 1, 2, and 3 steps. Each time you hit n,
    increment count. DP solution - same except cache each step count
    - linear time, linear space

total time: ~1hr
'''


def permutation_count_for_n_steps_recursive(n):
    # O(n^3)
    if n == 0:
        return 1
    if n < 0:
        return 0
    count1 = permutation_count_for_n_steps_recursive(n - 1)
    count2 = permutation_count_for_n_steps_recursive(n - 2)
    count3 = permutation_count_for_n_steps_recursive(n - 3)
    return count1 + count2 + count3


def permutation_count_for_n_steps_dp(n, step_count):
    # O(n)
    if n == 0:
        return 1
    if n < 0:
        return 0
    count1 = step_count.get(n - 1)
    if not count1:
        count1 = permutation_count_for_n_steps_dp(n - 1, step_count)
        step_count[n - 1] = count1
    count2 = step_count.get(n - 2)
    if not count2:
        count2 = permutation_count_for_n_steps_dp(n - 2, step_count)
        step_count[n - 2] = count2
    count3 = step_count.get(n - 3)
    if not count3:
        count3 = permutation_count_for_n_steps_dp(n - 3, step_count)
        step_count[n - 3] = count3
    return count1 + count2 + count3


step_size = 28
# print permutation_count_for_n_steps_recursive(step_size)
step_count = {}
print permutation_count_for_n_steps_dp(step_size, step_count)
