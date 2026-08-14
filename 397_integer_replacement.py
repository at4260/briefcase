# similar to fibonacci number or climbing stairs
# using a counter would be binding a local variable to use inside a nested function
# mutating a local variable is ok (like adding to a hash map), counter binds to a new
# local var since integers are immutable, which is not ok for nested functions
# unless you make it a global variable (nonlocal/global)

class Solution:
    def integerReplacement(self, n: int) -> int:
        # mod 4 solution - bitwise manipulation
        # O(log n) time, O(1) space
        counter = 0
        while n != 1:
            counter += 1
            if n % 2 == 0:
                n /= 2
            else:
                if n % 4 == 3 and n != 3:
                    n += 1 # going up is better sometimes, but not all times and never worse, except for 3
                else:
                    n -= 1

        return counter

        # naive dfs
        # O(log n) time, O(log n) space - branching only happens at odds, not branching by 2 at every level
        # def dfs(val):
        #     if val == 1:
        #         return 0

        #     if val % 2 == 0:
        #         return 1 + dfs(val / 2)
        #     else:
        #         return 1 + min(dfs(val - 1), dfs(val + 1))

        # return dfs(n)

        # cache 
        # O(log n) time, O(log n) space - memoization doesn't benefit much because numbers constantly reducing
        # so nothing cached gets reused often
        cache = {}
        def dfs(val):
            if val == 1:
                return 0
            if val in cache:
                return cache[val]

            if val % 2 == 0:
                res = 1 + dfs(val / 2)
            else:
                res = 1 + min(dfs(val - 1), dfs(val + 1))
            cache[val] = res
            return res

        return dfs(n)