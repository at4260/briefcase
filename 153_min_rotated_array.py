
def findMin(nums: List[int]) -> int:
	# Test cases
	# nums = [4,5,6,7,0,1,2] => 0
	# nums = [4,5,6,7] => 4
	# nums = [1] => 1

	# brute force - search through entire list
	# On space, O1 space

	# optimal - binary search
	# O log n time, O1 space
	left, right = 0, len(nums) - 1
	min_val = nums[0] # has to be one of the values in the array, let's see if we can beat it
	
	while left <= right:
		mid = (left + right) // 2

		if nums[left] <= nums[mid]: # left sorted array
			# smallest value has to be nums[left]
			min_val = min(min_val, nums[left])
			left = mid + 1
		else: # right sorted array
			min_val = min(min_val, nums[mid])
			right = mid - 1

	return min_val


nums = [4,5,6,7,0,1,2]
res = findMin(nums)
print('Results: ', res)	
