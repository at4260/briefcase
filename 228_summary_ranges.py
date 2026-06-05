class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # O(n) time, O(1) space exc output array
        res = []
        start_marker = None

        for i in range(len(nums)):

            if i == len(nums) - 1 or nums[i] + 1 != nums[i+1]:
                if start_marker is None:
                    res.append(str(nums[i])) 
                else:
                    res.append(f"{start_marker}->{nums[i]}")
                    start_marker = None
            else:
                if start_marker is None:
                    start_marker = nums[i]
    
        return res

    # better code
    def summaryRanges(self, nums):
        res = []
        start = 0
        
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] + 1 != nums[i+1]:
                if nums[start] == nums[i]:
                    res.append(str(nums[i]))
                else:
                    res.append(f"{nums[start]}->{nums[i]}")
                start = i + 1
        
        return res
    