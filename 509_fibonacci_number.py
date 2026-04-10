class Solution:
    def fib(self, n: int) -> int:
        # recursive; O(2^n) time for recalculating the same function multiple times, O(n) space for recursive stack
        if n == 1:
            return 1
        if n == 0:
            return 0

        return self.fib(n-1) + self.fib(n-2)