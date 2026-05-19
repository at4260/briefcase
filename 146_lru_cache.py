class LRUCache:

    # O(1) time for each function, O(n) space
    # we need to both update key-val pairs and update LRU in O(1) time
        # updating key-val => hash map
        # LRU requires both adding to front of list and evicting or moving a key-val pair to front => doubly linked list
            # standard: head -> MRU ----> LRU -> tail
        # alternatives:
            # deque (fifo) can do O(1) operations but cannot update a key-val pair in O(1) time
            # hash map alone can do key-val pair updates in O(1) but cannot track order
            # singly linked list would require traversing the list to get the previous node
            # hash map with an stack/deque would require O(n) when re-accessing a random node moves it to the front/back of list

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # key: node
        # doubly linked list
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node):
        # remove node from linked list and relink around it
        left = node.prev
        right = node.next
        left.next = right
        right.prev = left

    def add(self, node):
        # add node to beginning of linked list - becomes MRU
        tmp = self.head.next # original next node
        node.prev = self.head
        node.next = tmp
        self.head.next = node
        tmp.prev = node

    def get(self, key: int) -> int:
        # get the value and move key-val to MRU position
        node = self.cache.get(key)
        if node:
            # update LRU - remove from current position and move to MRU
            self.remove(node)
            self.add(node)

            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        # update the value and move key-val to MRU position
        node = self.cache.get(key)
        if node:
            node.val = value 

            # update LRU - remove from current position and move to MRU
            self.remove(node)
            self.add(node)
        else:
            # evict LRU if exceeds capacity
            if len(self.cache.keys()) == self.capacity:
                lru_node = self.tail.prev
                self.remove(lru_node)
                # remove from hash map
                self.cache.pop(lru_node.key)

            # add new node
            new = Node(key, value)
            self.add(new)
            # add to hash map
            self.cache[key] = new
        

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)