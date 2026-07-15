class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # On time, On space
        # newnums = [num for num in nums]
        # for i in range(len(newnums)):
        #     newi = (i + k) % len(nums)
        #     nums[newi] = newnums[i]

        # in place reassignment, track how many elements have changed to determine when
        # to stop
        # also have scenario where if len(nums) is divisible by k, it will swap the same two 
        # values infinitely so need to track if we landed back at the start to move the start
        # pointer forward
        # On time, O1 space
        # count = 0
        # start = 0

        # while count < len(nums):
        #     prev = (start, nums[start]) 
        #     while True:
        #         new_i = (prev[0] + k) % len(nums) 
        #         new_val = prev[1]
        #         prev = (new_i, nums[new_i]) 
        #         nums[new_i] = new_val
        #         count += 1

        #         if new_i == start:
        #             start += 1
        #             break
                

        # reverse [1,2,3,4,5,6,7], k = 4 => [7,6,5,4,|3,2,1]
        # split array into two parts after kth element and reverse back
        # [4,5,6,7,1,2,3]
        # On time, O1 space

        k = k % len(nums) # when k > len(nums) like nums = [-1] and k = 2
        def reverse(vals, start, end):
            left, right = start, end
            while left < right:
                tmp = vals[right]
                vals[right] = vals[left]
                vals[left] = tmp
                # vals[left], vals[right] = vals[right], vals[left] simultaneous assignment
                left += 1
                right -= 1

        reverse(nums, 0, len(nums) - 1)
        reverse(nums, 0, k - 1)
        reverse(nums, k, len(nums) - 1)
