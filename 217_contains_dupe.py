def test_func(nums: list) -> bool:
	# seen = {}
	# for x in nums:
	# 	if x in seen:
	# 		return True
	# 	else:
	# 		seen[x] = 1 
	# return False
    
	# use a set instead of a map since we don't care about values
	seen = set()
	for x in nums:
		if x in seen:
			return True
		else:
			seen.add(x)
	return False
 

s = [1,2,5,3,4,5]			
res = test_func(s)
print('Results: ', res)	
