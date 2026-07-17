class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # brute force dfs 
        # O(2^n+m) time since visiting and recomputing a cell potentially multiple times
        # O(m+n) space
        # def dfs(r, c):
        #     if r < 0 or r > m or c < 0 or c > n:
        #         return 0
        #     if r == m - 1 and c == n - 1:
        #         return 1

        #     return dfs(r+1, c) + dfs(r, c+1)

        # return dfs(0,0)

        # memoization
        # O(n*m) time (compute each cell once), O(n*m) space (cache stores a value per cell)
        # cache = {} # (r,c): value
        # def dfs(r, c):
        #     if (r,c) in cache:
        #         return cache[(r,c)]
        #     if r < 0 or r > m or c < 0 or c > n:
        #         return 0
        #     if r == m - 1 and c == n - 1:
        #         return 1

        #     value = dfs(r+1, c) + dfs(r, c+1)
        #     cache[(r,c)] = value
        #     return value

        # return dfs(0,0)   

        # dp solution - start from the base case and build up
        # each cell's value represents the number of paths to the end available from
        # that cell (right cell value + down cell value)
        # all bottom row and right column will be 1 since there's only 1 path available
        # from those cells to the goal
        # O(n*m) time, O(n*m) space
        # ex: m = 3, n = 2 => 3
            # [
            #   [1+2=3,1]
            #   [1+1=2,1]
            #   [1,1]
            # ]

        dp = [([1] * n) for i in range(m)] # create initial grid

        # move from bottom right to top left and only overwrite starting at 2nd cell 
        # from bottom right
        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1): 
                dp[r][c] = dp[r+1][c] + dp[r][c+1]

        return dp[0][0]


        # O(n*m) space, reduces to O(n) space if we only hold a single row and 
        # update in place
        dp = [1] * n

        for r in range(m - 2, -1, -1):
            for c in range(n - 2, -1, -1):
                dp[c] = dp[c] + dp[c+1]

        return dp[0]
