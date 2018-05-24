'''
Problem: Write an function that takes in an start string and end string. The function should return
    the shortest edit distance algorithm that transforms start to end. Bonus points for supplying
    the edits it would take. Note that SWAP == ADD == DELETE == 1 (cost of all edits is equal)

total time: 1hr just distance; 1.5hrs with edit path
'''
MATCH, SWAP, INSERT, DELETE = 1, 2, 3, 4


class DistanceCost:
    edit = 0  # MATCH, INSERT, DELETE
    cost = 0


def _print_path(distance_cost_matrix):
    path = ''
    i, j = len(distance_cost_matrix) - 1, len(distance_cost_matrix[0]) - 1
    while i != 0 or j != 0:
        current = distance_cost_matrix[i][j]
        if current.edit == MATCH:
            path = 'M' + path
            i, j = i - 1, j - 1
        elif current.edit == SWAP:
            path = 'S' + path
            i, j = i - 1, j - 1
        elif current.edit == INSERT:
            path = 'I' + path
            i, j = i - 1, j
        elif current.edit == DELETE:
            path = 'D' + path
            i, j = i, j - 1
    print path


def edit_distance(start, end):
    start = ' ' + start
    end = ' ' + end
    distance_cost_matrix = (
        [[DistanceCost() for _ in xrange(len(start))] for _ in xrange(len(end))])

    for j in xrange(len(start)):
        distance_cost_matrix[0][j].cost = j
        distance_cost_matrix[0][j].edit = DELETE
    for i in xrange(len(end)):
        distance_cost_matrix[i][0].cost = i
        distance_cost_matrix[i][0].edit = INSERT

    for i in xrange(1, len(end)):
        for j in xrange(1, len(start)):
            current = distance_cost_matrix[i][j]
            current.edit = SWAP
            current.cost = distance_cost_matrix[i-1][j-1].cost + 1

            insert = distance_cost_matrix[i][j-1]
            delete = distance_cost_matrix[i-1][j]
            if start[j] == end[i]:
                current.edit = MATCH
                current.cost = distance_cost_matrix[i-1][j-1].cost
            if insert.cost + 1 < current.cost:
                current.edit = INSERT
                current.cost = insert.cost + 1
            if delete.cost + 1 < current.cost:
                current.edit = DELETE
                current.cost = delete.cost + 1

    _print_path(distance_cost_matrix)
    return distance_cost_matrix[-1][-1].cost


start = 'thou shalt not'
end = 'you should not'
print edit_distance(start, end)
