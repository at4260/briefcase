class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        # On space, On time
        num_eat = len(candyType) // 2
        candy_set = set(candyType) # {1,2,3} # On operation
        return min(num_eat, len(candy_set))
