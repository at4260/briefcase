
def search(nums: List[int], target: int) -> int:
	# Test cases
	# nums = [4,5,6,7,0,1,2], target = 0 => 4
	# nums = [4,5,6,7,0,1,2], target = 3 => -1
	# nums = [1], target = 0 => -1

	# brute force - search through entire list
	# On space, O1 space

	# optimal - binary search
	# O log n time, O1 space
	left, right = 0, len(nums) - 1
	while left <= right:
		mid = (left + right) // 2
		
		if nums[mid] == target:
			return mid
		
		if nums[mid] >= nums[left]: # sorted array on the left side; floor div always rounds down towards left
			if nums[left] <= target < nums[mid]:
				right = mid - 1 # target is on the left side
			else:
				left = mid + 1 # target must be on right side in unsorted array
		else: # sorted array on the right side
			if nums[mid] < target <= nums[right]:
				left = mid + 1 # target is on the right side
			else:
				right = mid - 1 # target must be on left side in unsorted array
		
	return -1


nums = [4,5,6,7,0,1,2]
target = 9
res = search(nums, target)
print('Results: ', res)	
