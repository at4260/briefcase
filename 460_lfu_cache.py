# O(1) time for each function, O(n) space
# build on LRU cache with dict and linked list
# the major difference is we have a counter so we need a way to access the counter value to move nodes when we access them.
# when there's a tie in counts, we evict the LRU, so we need a way to order the nodes in { counter: [list of nodes] }. 
# so we're back at using linked lists and it becomes we have a linked list per counter value
# where when we move nodes around, we remove it from the counter = 1 linked list and move it to the counter = 2 linked list
# we maintain a freq_count so we're able to remove the LFU node from the smallest count in O(1) time. otherwise, we need to
# get the smallest counter in our dict (O(n))

class Node:
    def __init__(self, key, value):
        self.key = key
        self.val = value
        self.counter = 0
        self.next = None
        self.prev = None

class LFUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.freq_cache = {} # counter: [self.head, self.tail]
        # smallest counter value in freq_cache could be linked list with nothing but head and tail, 
        # so this tells us which freq_cache has a linked list we care about
        self.min_freq = 0 
        self.cache = {} # key: node

    def get(self, key: int) -> int:
        # lookup in dict
        curr_node = self.cache.get(key)
        if not curr_node:
            return -1

        self.remove_node(curr_node)

        if self.is_bucket_empty(curr_node.counter):
            if curr_node.counter == self.min_freq:
                self.min_freq += 1

        curr_node.counter += 1
        self.move_to_new_freq_bucket(curr_node)

        return curr_node.val

    def put(self, key: int, value: int) -> None:
        # lookup in dict - if exists, update key, increase counter by 1 and move node
        curr_node = self.cache.get(key)
        if curr_node:
            curr_node.val = value
            self.remove_node(curr_node)

            if self.is_bucket_empty(curr_node.counter):
                if curr_node.counter == self.min_freq:
                    self.min_freq += 1

            curr_node.counter += 1
            self.move_to_new_freq_bucket(curr_node)

        # if doesn't exist, check capacity before inserting
            # if exceeds capacity, drop first node (LFU and LRU), delete from dict, add new dict entry, create new node and add to right of node with same counter value
            # if doesn't exceed capacity, add new dict entry, create new node and add to right of node with same counter value
        else:
            if self.capacity <= len(self.cache): 
                head, tail = self.freq_cache[self.min_freq]
                lru_node = head.next
                del(self.cache[lru_node.key])
                self.remove_node(lru_node)

            new_node = Node(key, value)
            new_node.counter = 1
            self.min_freq = 1
            self.cache[key] = new_node
            self.move_to_new_freq_bucket(new_node)

        
    def remove_node(self, curr_node):
        # remove node 
        left = curr_node.prev
        right = curr_node.next
        left.next = right
        right.prev = left
        
    def add_to_end(self, curr_node, tail):
        # add node to before tail
        left = tail.prev
        left.next = curr_node
        curr_node.prev = left
        curr_node.next = tail
        tail.prev = curr_node

    def move_to_new_freq_bucket(self, curr_node):
        if self.freq_cache.get(curr_node.counter): # new freq bucket exists
            # move to end of new counter LL
            head, tail = self.freq_cache[curr_node.counter]
            self.add_to_end(curr_node, tail)
        else: # new bucket doesn't exist yet - create new linked list and add to freq_cache
            head = Node(0,0)
            tail = Node(0,0)
            head.next = curr_node
            curr_node.prev = head
            curr_node.next = tail
            tail.prev = curr_node

            self.freq_cache[curr_node.counter] = [head, tail]        

    def is_bucket_empty(self, counter):
        head, tail = self.freq_cache[counter]
        return head.next == tail
    

        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)