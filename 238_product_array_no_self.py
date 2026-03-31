
def productExceptSelf(self, nums: List[int]) -> List[int]:
	# Test cases
	# nums = [1,2,3,4] => [24,12,8,6]
	# nums = [-1,1,0,-3,3] => [0,0,9,0,0]

	# On2 time, On space
	vals = []
	for i in range(len(nums)):
		total = 1
		for j in range(len(nums)):
			if i == j:
				continue
			total *= nums[j]
			
		vals.append(total)

	return vals

	# using divison operator
	# On time, On space
	vals = []
	total = 1
	nozerototal = 1
	for num in nums:
		if num != 0:
			nozerototal *= num
		total *= num

	for num in nums:
		if num == 0: # 0/0 results in zero error 
			vals.append(nozerototal)
		else:
			vals.append(total // num) 

	return vals

	# prefix, suffix
	# On time, On space
	prefixes = [1] * len(nums)
	suffixes = [1] * len(nums)
	vals = []

	for i in range(1, len(nums)):
		prefixes[i] = prefixes[i - 1] * nums[i - 1]

	for i in range(len(nums) - 2, -1, -1): # move right to left
		suffixes[i] = suffixes[i + 1] * nums[i + 1]    
		
	for i in range(len(nums)):
		vals.append(prefixes[i] * suffixes[i])

	return vals

	# prefix, suffix in place
	# On time, O1 space
	vals = [1] * len(nums)
	suffix = 1

	for i in range(1, len(nums)):
		vals[i] = vals[i - 1] * nums[i - 1]

	for i in range(len(nums) - 2, -1, -1): # move right to left
		suffix = suffix * nums[i + 1]
		vals[i] = vals[i] * suffix

	return vals        


nums = [1,2,3,4]
res = productExceptSelf(nums)
print('Results: ', res)	
