class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort, then find
        # On logn time, O1 space
        # nums.sort()

        # length = 0
        # max_length = 0

        # for i in range(len(nums)):
        #     if i == 0:
        #         length += 1
        #         max_length += 1
        #         continue
            
        #     if nums[i-1] + 1 == nums[i]:
        #         length += 1
        #     elif nums[i-1] == nums[i]: # dupe
        #         continue
        #     else:
        #         length = 1

        #     max_length = max(max_length, length)

        # return max_length


        # On time, On space
        max_length = 0
        nums_set = set(nums)
        for num in nums_set:
            if num - 1 in nums_set:
                continue
            else:
                length = 1
                while (num + length) in nums_set:
                    length += 1
                max_length = max(max_length, length)

        return max_length
