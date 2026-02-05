
def searchInsert(nums: List[int], target: int) -> int:
	# Test cases
	# nums = [-1,0,3,5,9,12], target = 9 => 4
	# nums = [-1,0,3,5,9,12], target = 2 => 2
	# nums = [-1], target = 9 => 1
	# nums = [-1], target = -2 => 0

	# brute force - search through entire list
	# O n space, O1 space

	# optimal - binary search
	# O log n time, O1 space
	left, right = 0, len(nums) - 1
	while left <= right:
		# if concerned about overflow (not a python issue), can do mid = l + ((r - l) // 2)
		mid = (left + right) // 2
		if nums[mid] > target:
			right = mid - 1
		elif nums[mid] < target:
			left = mid + 1
		else: # nums[mid] == target
			return mid
		
	return left


nums = [-1,0,3,5,9,12]
target = 9
res = searchInsert(nums, target)
print('Results: ', res)	
