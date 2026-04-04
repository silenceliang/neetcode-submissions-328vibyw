class LinkedList:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # keep a linkedlist with length capacity
    # get: fetch from dict and move it to the head
    # put: put it to the head
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = LinkedList(0,0)
        self.tail = LinkedList(0,0)
        self.head.prev, self.tail.next = self.tail, self.head
        self.head.next, self.tail.prev = self.tail, self.head
        self.d = {}

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.delete_node(key)
            self.add_node(key, node.val)
            return node.val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.d:
             self.delete_node(key)

        if len(self.d) == self.capacity:
            # delete tail
            tail = self.tail.prev
            self.delete_node(tail.key)

        self.add_node(key, value)

    def add_node(self, key, val):
        # add into dict
        node = LinkedList(key, val)
        # put on top
        node.next, node.prev = self.head.next, self.head
        self.head.next.prev, self.head.next = node, node
        self.d[key] = node
    
    def delete_node(self, key):
        node = self.d[key]
        node.prev.next, node.next.prev = node.next, node.prev
        self.d.pop(key)


