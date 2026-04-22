class Solution:
    def climbStairs(self, n: int) -> int:
        
		# O2^n time, On space
        # returned value represents number of possible combinations when given n steps
        if n == 1:
            return 1
        if n == 2:
            return 2

        return self.climbStairs(n-1) + self.climbStairs(n-2)

        # top down dp (memoization)
        # On time, On space
        cache = {}
        def dfs(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n in cache:
                return cache[n]

            cache[n] = dfs(n-1) + dfs(n-2) 
            return cache[n]
        return dfs(n)
    