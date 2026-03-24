nums = [3,2,1,3,3]


def majorityElement(nums):
	# On time, 0n space
	counts = {}
	for val in nums:
		counts[val] = counts.get(val, 0) + 1

	res = [k for k,v in counts.items() if v == max(counts.values())]
	return res[0]

	# boyer moore voting algorithm - increment/decrement and when it hits 0, we set a new candidate
	# O(n) time, O(1) space
	candidate = None
	count = 0
	for num in nums:
		if count == 0:
			candidate = num
		if candidate == num:
			count += 1 
		else:
			count -= 1

	return candidate
			
res = majorityElement(nums)
print('Results: ', res)	
