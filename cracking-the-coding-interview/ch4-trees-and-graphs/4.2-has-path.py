'''
Problem: Given a directed graph, find whether there is a path between two nodes
Solution: BFS for target including visited set to avoid cycle infinit loops
    - linear time, linear space

total time: 10 min

struggles:
    - assumed list.push(*array) was a thing. push isn't even a thing. append works for single
        elements. list.extend(array) is what I was looking for (extend list with elements in array)
    - forgot that list.pop() pops from the right (how unintuitive...). deque.popleft() is best
'''
from collections import deque


# assumed graph node structure
class GraphNode(object):
    data = None
    adjacent_nodes = ['node b', 'node c']


def has_path(start, target):
    visited = set()
    to_visit = deque()

    to_visit.append(start)
    while len(to_visit):
        node = to_visit.popleft()
        if node in visited:
            continue
        visited.add(node)
        if node.data == target.data:
            return True
        to_visit.extend(node.adjacent_nodes)

    return False
