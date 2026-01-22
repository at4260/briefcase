nums = [3,2,1,3,3]


def majorityElement(nums):
	# On time, 0n space
	counts = {}
	for val in nums:
		counts[val] = counts.get(val, 0) + 1

	res = [k for k,v in counts.items() if v == max(counts.values())]
	return res[0]

			
res = majorityElement(nums)
print('Results: ', res)	
