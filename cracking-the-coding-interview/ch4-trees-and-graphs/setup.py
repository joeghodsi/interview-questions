class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "( " + str(self.data) + " ( " + str(self.left) + " | " + str(self.right) + "))"
