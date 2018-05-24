'''
I fucked this problem up beacuse I didn't think about the fact that an unbalanced tree of just a
line of left nodes is ...unbalanced. My train of thought was check the min/max heights when I hit
each leaf and if the difference between min and max is more than one, it's an unbalanced tree
'''

import random
from setup import Node


def is_balanaced(root, min_height={}, max_height={}, current_height=0):
    if not root:
        return
    if root.left:
        if not is_balanaced(root.left, min_height, max_height, current_height + 1):
            return False
    if root.right:
        if not is_balanaced(root.right, min_height, max_height, current_height + 1):
            return False
    if not (root.left or root.right):  # leaf
        if not min_height.get('data') or current_height < min_height['data']:
            min_height['data'] = current_height
        if not max_height.get('data') or current_height > max_height['data']:
            max_height['data'] = current_height
        if max_height['data'] - min_height['data'] > 1:
            return False
    return True


# Testing

# building testcase 1 - linear tree down the left side
bt = Node(random.randint(0, 100))
for _ in xrange(0, 19):
    bt2 = Node(random.randint(0, 100))
    bt2.left = bt
    bt = bt2

test1_unbalanced = bt


# building testcase 2
def make_random_balanced_tree(depth, i=1):
    if depth > 0:
        tree = Node(i)
        tree.left = make_random_balanced_tree(depth-1, i+1)
        tree.right = make_random_balanced_tree(depth-1, i+2)
        return tree
    else:
        return None

test2_balanced = make_random_balanced_tree(5)

# building testcase 3
test3_balanced = Node(random.randint(0, 100))
test3_balanced.left = Node(random.randint(0, 100))
test3_balanced.left.right = Node(random.randint(0, 100))
test3_balanced.right = Node(random.randint(0, 100))
test3_balanced.right.left = Node(random.randint(0, 100))
test3_balanced.right.right = Node(random.randint(0, 100))
test3_balanced.right.right.right = Node(random.randint(0, 100))

# building testcase 4 - left depth is 2, right depth is 4 at the very rightmost
test4_unbalanced = Node(1)
test4_unbalanced.left = Node(2)
test4_unbalanced.left.right = Node(3)
test4_unbalanced.right = Node(4)
test4_unbalanced.right.left = Node(5)
test4_unbalanced.right.right = Node(6)
test4_unbalanced.right.right.right = Node(7)
# this unbalances it
test4_unbalanced.right.right.right.right = Node(8)

# building testcase 5
test5_unbalanced = Node(1)
test5_unbalanced.left = Node(2)
test5_unbalanced.left.right = Node(3)
test5_unbalanced.right = Node(4)
test5_unbalanced.right.right = Node(5)
test5_unbalanced.right.right.right = Node(6)


if not is_balanaced(test1_unbalanced, {}, {}):
    print "Test 1 passed"
else:
    print "Test 1 not passed"
if is_balanaced(test2_balanced, {}, {}):
    print "Test 2 passed"
else:
    print "Test 2 not passed"
if is_balanaced(test3_balanced, {}, {}):
    print "Test 3 passed"
else:
    print "Test 3 not passed"
if not is_balanaced(test4_unbalanced, {}, {}):
    print "Test 4 passed"
else:
    print "Test 4 not passed"
if not is_balanaced(test5_unbalanced, {}, {}):
    print "Test 5 passed"
else:
    print "Test 5 not passed"
