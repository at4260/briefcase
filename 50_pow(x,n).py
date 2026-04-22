class Solution:
    def myPow(self, x: float, n: int) -> float:
        # brute force
        # On time, O1 space
        if x == 0:
            return 0
        if n == 0:
            return 1
        
        result = 1
        for i in range(abs(n)):
            result *= x
        if n < 0:
            return 1/result
        
        return result


        # must double the base to halve the power in that order for O(log n) time. ex: 3^12 => (3^2)^6, not (3^6)^2
        # binary iterative - O(log n) time, O(1) space
        if x == 0:
            return 0
        if n == 0:
            return 1

        result = 1
        power = abs(n)
        while power:
            if power % 2 == 1: # odd
                result *= x
            x *= x # x^2
            power = power // 2

        if n < 0:
            return 1/result
        
        return result        


        # half the exponent to the base case and square it each time you come back up the call stack
        # binary recursive - O(log n) time, O(1) space
        def helper(x: float, n: int) -> float:
            if n == 0:
                return 1

            res = helper(x, n // 2)
            if n % 2 == 1: # odd
                return x * res * res
            return res * res

        if x == 0:
            return 0

        result = helper(x, abs(n))

        if n < 0:
            return 1/result
        
        return result
