class MyQueue:

    # Python list already operates like a stack under the hood
    # so we can pop/append in O(1) time

    # standard
    # On space, O2n -> On time
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        # pop from stack1 into stack2
        # pop off last element in stack2 (stack1[0])
        # restore stack1 by popping off from stack2
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        
        res = self.stack2.pop()
        
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

        return res


    def peek(self) -> int:
        for i in range(len(self.stack1)):
            self.stack2.append(self.stack1.pop())
        
        res = self.stack2[-1] # "pull from top" is a stack operation so this index is acceptable here in O(1) time
        
        for i in range(len(self.stack2)):
            self.stack1.append(self.stack2.pop())

        return res
        

    def empty(self) -> bool:
        return not self.stack1 
    
    
    # amortized constant time - first time requires O(n) and each pop() after will be constant time
    # On space, On -> O1 time

    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


    def peek(self) -> int:
        if not self.stack2:
            for i in range(len(self.stack1)):
                self.stack2.append(self.stack1.pop())

        return self.stack2[-1] # allowable because similar to stack's top
        

    def empty(self) -> bool:
        return not self.stack1 and not self.stack2
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
