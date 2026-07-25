class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None 

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} 
        # key, value pair dictionary and value is a node
        self.left = Node(0, 0)
        # start with a dummy
        self.right = Node(0, 0)
        # start with a dummy

        self.left.next = self.right
        self.right.prev = self.left
        # double linked list
        
    def removeNode(self, node):
        prev = node.prev 
        nxt = node.next
        prev.next = nxt 
        nxt.prev = prev 

    def insertNode(self, node):
        prev = self.right.prev 
        nxt = self.right
        prev.next = node
        nxt.prev = node 
        node.next = nxt 
        node.prev = prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.removeNode(self.cache[key])
            self.insertNode(self.cache[key])
            # remove the node and add it to the right end
            return self.cache[key].value
            # the output 
        return -1 
        # otherwise nothing

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.removeNode(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insertNode(self.cache[key])

        if len(self.cache) > self.capacity:
            least_used = self.left.next
            # next because first node is a dummy
            self.removeNode(least_used)
            del self.cache[least_used.key]
        
