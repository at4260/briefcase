
def minSubArrayLen(target, nums):
	# brute force
	# on2 time, o1 space
	# min_length = len(nums) + 1
	# for left in range(len(nums)):
	#     total = nums[left]
	#     if total >= target:
	#         return 1
	#     for right in range(left + 1, len(nums)):
	#         total += nums[right]
	#         if total >= target:
	#             min_length = min(min_length, right - left + 1)

	# return 0 if min_length == len(nums) + 1 else min_length        

	# sliding window        
	min_length = len(nums) + 1
	left, total = 0, 0
	for right in range(len(nums)):    
		total += nums[right]
		while total >= target:
			min_length = min(min_length, right - left + 1)
			total -= nums[left]
			left += 1

	return 0 if min_length == len(nums) + 1 else min_length 

	# O(n log n) solution - generate a prefix array
	# nums = [2,3,1,2,4,3], prefixes = [0,3,5,6,8,12,15]
	# goal - prefix[i] = target -> since once we remove the values to the left, we would remove that sum from the current prefix sum
	# ex: i = 2 (represents val 1), goal = target + prefixes[2] = 7 + 5 = 12. We are going to binary search for a sum of 12 stopping 
	# at prefixes[5] so 5-2 = 3 length representing subarray [1,2,4]
	res = float("inf")
	
	prefixes = [0]
	for num in nums:
		prefixes.append(prefixes[-1] + num)

	for i in range(len(nums)):
		goal = target + prefixes[i]
		# binary search on i + 1
		left = i + 1
		right = len(prefixes) - 1
		while left < right:
			mid = (left + right) // 2
			if prefixes[mid] == goal:
				res = min(res, mid - i)
				break
			elif prefixes[mid] > goal:
				right = mid
			else: # prefixes[mid] < goal
				left = mid + 1
		if left == right and prefixes[right] >= goal:
			res = min(res, right - i)

	return 0 if res == float("inf") else res
            	

target = 11
nums = [1,1,1,1,1]
# target = 7
# nums = [2,3,1,2,4,3]
res = minSubArrayLen(target, nums)
print('Results: ', res)	
