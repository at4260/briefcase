class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        # loop and compare to number before
            # if nums[i] <= nums[i-1] -> invalid
        # if invalid, detemrine which value to remove
            # to remove nums[i-1]: check if nums[i-2] < nums[i]
            # to remove nums[i]: check if nums[i-1] < nums[i+1]
            # if both fail, return False

        # On time, O1 space
        removed = False
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]: # invalid val
                if removed: # a value has already been removed
                    return False

                removed = True
                if i != 1 and i != len(nums) - 1: # out of bounds
                    prev_val_check = nums[i-2] < nums[i]
                    curr_val_check = nums[i-1] < nums[i+1]
                    if not prev_val_check and not curr_val_check: # no safe removals
                        return False

        return True
