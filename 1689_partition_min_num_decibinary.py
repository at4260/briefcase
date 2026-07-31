class Solution:
    def minPartitions(self, n: str) -> int:
        # 32 = 11+ 11+ 10
        # 82734
            # 11111 + 10111 + 10111 + 10101 + 10100 + 10100 + 10100 + 10000
        # sum by each individual digit, so answer is the max value in n


        # On time, O1 space
        res = 0
        for num in n:
            res = max(int(num), res)

        return res
