class Solution:
    def minMoves(self, nums: List[int]) -> int:

        # to increment by 1 n-1 elements is equivalent to decrement by 1 a single element
        # in that case, if you can only decrement one number, the max number is always going to decrement down
        # to the smallest value in the array
            # therefore, we can calc this by summing the difference of all values in the array and the min value

#         [1,2,3]            
#         1.2.2 
#         1.2.1 
#         1.1.1 

#         decrementing 1 element by 1
#         [1,1,3,5]
#         1.1.3.4
#         1.1.3.3
#         1.1.2.3
#         1.1.2.2
#         1.1.1.2
#         1.1.1.1

#         is same as incrementing n-1 elements by 1
#         1.1.3.5
#         2.2.4.5
#         3.3.5.5
#         4.4.5.6
#         5.5.6.6
#         6.6.6.7
#         7.7.7.7

        # O(2n) time
        diff = 0 
        min_val = min(nums)
        for num in nums:
            diff += num - min_val
        return diff

        # O(1n) time
        # keep running total and find min at same time, get difference between total and min * len of list 
        # for sum of each value's diff
        total = 0
        min_val = nums[0]
        for num in nums:
            total += num
            min_val = min(min_val, num)
        return total - (len(nums) * min_val)
