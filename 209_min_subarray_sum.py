
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

	# O(n log n) solution - ??

target = 11
nums = [1,1,1,1,1]
# target = 7
# nums = [2,3,1,2,4,3]
res = minSubArrayLen(target, nums)
print('Results: ', res)	
