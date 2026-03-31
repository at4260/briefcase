

def removeDupes(nums: list) -> int:
    # brute force
    # create a set from the array and len(set(num))
    # On time, On space => not modified in place

    # On2 time due to the pop, O1 space, remove in place => two pointers
    # left, right = 0, 1
    # while right < len(nums):
    #     if nums[left] == nums[right]:
    #         nums.pop(right)
    #     else:
    #         left += 1
    #         right += 1

    # return len(nums)

    # two pointers - find the next nondupe and assign to left pointer's spot
    # o1 space, on time
    left = 0
    right = 0
    while right < len(nums):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
        right += 1

    return left + 1


nums = [0,0,1,1,1,2,3,3,4]			
res = removeDupes(nums)
print('Results: ', res)	
# res = [0,1,2,3,4,_,_,_,_,_]
