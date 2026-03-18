# REVIEW

from collections import deque # "deck" double ended queue

class MyStack:

    # deque is Python's queue so we can pop/append from the left in 0(1) time
    # plus everything a list already does like pop/append from the right is also O(1)
    # Note: we don't use Python list here because .pop(0) is O(n) time - removes the
    # first element then needs to go thru the list to reshift all elements forward

    # standard
    # On space, On time
    # pop off the front of the queue and move it to the back until the last value is now in [0]
    # call front of the queue to get the back of the stack

    def __init__(self):
        self.queue1 = deque()
        

    def push(self, x: int) -> None:
        self.queue1.append(x)
        

    def pop(self) -> int:
        max_swaps = len(self.queue1) - 1
        for i in range(max_swaps):
            self.queue1.append(self.queue1.popleft()) # queue's "top"
        return self.queue1.popleft()
        

    def top(self) -> int:
        return self.queue1[-1]
        # indexing on front and back for deque is o(1); indexing anywhere else is o(n)
        # contrast to indexing anywhere on a list is o(1)
        

    def empty(self) -> bool:
        return not self.queue1
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()