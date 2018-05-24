'''
Problem: Design and implement a hash table that uses chaining for collision

total time: 1.5hrs buggy; 2hrs finished
'''
from random import randint


class Node:
    def __init__(self, key=None, data=None):
        self.key = key
        self.data = data
        self.next = None
        return

    def __repr__(self):
        node = self
        print_val = ''
        while node.next is not None:
            print_val += '(%s, %s) -> ' % (node.key, node.data)
            node = node.next
        print_val += '(%s, %s)' % (node.key, node.data)
        return print_val

    def __len__(self):
        count = 0
        node = self
        while node is not None:
            count += 1
            node = node.next
        return count

    def get_node(self, data):
        node = self
        while node is not None:
            if node.data == data:
                return node
            node = node.next
        return None


def create_list_from_array(arr):
    head = Node(data=arr.pop(0))
    current = head
    for val in arr:
        current.next = Node(data=val)
        current = current.next
    return head


class HashTable:
    PRIMES = create_list_from_array([53, 97, 193, 389, 769, 1543, 3079])
    HASHING_PRIME = PRIMES  # http://planetmath.org/goodhashtableprimes
    SPARCITY_THRESHOLD = 0.4  # if data is this full, increase size to next prime

    def __init__(self):
        self._init()

    def get(self, key):
        llist = self.data[self._hash(key)]
        if llist is None:
            raise KeyError(key)
        node = llist
        while node is not None:
            if node.key == key:
                return node.data

    def put(self, key, value):
        index = self._hash(key)
        llist = self.data[index]
        if llist is None:
            self.data[index] = Node(key, value)
        elif self._list_size(index) > 0:
            node = llist
            while node is not None:
                if node.key == key:
                    # updating value for previously entered key
                    node.data = value
                    break
                node = node.next
            else:
                # append to collision list
                llist.next = Node(key, value)

        self.size += 1
        if self._should_resize():
            self._resize()

    def _init(self):
        self.size = 0
        self.data = [None] * self.HASHING_PRIME.data

    def _hash(self, key):
        return hash(key) % self.HASHING_PRIME.data

    def _percent_full(self):
        return float(self.size) / self.HASHING_PRIME.data

    def _should_resize(self):
        return self._percent_full() > self.SPARCITY_THRESHOLD

    def _resize(self):
        print '--------incurring resize slowdown--------'
        self.HASHING_PRIME = self.HASHING_PRIME.next
        if self.HASHING_PRIME is None:
            raise NotImplementedError('impl a next_ideal_prime algo - ran out of statics')

        nodes = []
        for llist in self.data:
            node = llist
            while node is not None:
                nodes.append(node)
                node = node.next

        self._init()
        for node in nodes:
            self.put(node.key, node.data)

    def _list_size(self, index):
        return len(self.data[index])

    def __repr__(self):
        print_val = ''
        for llist in self.data:
            print_val += llist.__repr__() + '\n'
        return print_val


table = HashTable()
table.put(1, 'a')
table.put(2, 'b')
print table.get(1)
table.put('abc yeah you know me', 'Michael Jackson')
print table.get('abc yeah you know me')
table.put('abc yeah you know me', 123)
print table.get('abc yeah you know me')
print '--------'
print table

table = HashTable()
for i in xrange(20):
    key = randint(100, 200)
    value = randint(100, 200)
    table.put(key, value)
print table
