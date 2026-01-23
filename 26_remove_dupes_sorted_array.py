

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

    # three pointers
    # o1 space, on time
    k = 1 # tracks the next non-dupe we see, also holds the number of unique elements
    i = 0 # left pointer
    j = 0 # right pointer

    while j < len(nums):
        if nums[i] != nums[j]:
            nums[k] = nums[j]
            k += 1 
        i += 1 
        j += 1 

    return k


nums = [0,0,1,1,1,2,3,3,4]			
res = removeDupes(nums)
print('Results: ', res)	
# res = [0,1,2,3,4,_,_,_,_,_]
