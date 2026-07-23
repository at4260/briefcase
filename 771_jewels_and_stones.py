class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # On time, On space
        count = 0
        jewels_set = set(jewels)
        for stone in stones:
            if stone in jewels_set: # O1 lookup
                count += 1

        return count

        # return sum(1 for stone in stones if stone in jewels_set)
        