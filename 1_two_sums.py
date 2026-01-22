# values = [3,2,-1,0,1,7]
values = [3, 2, 3]
target = 6


def twoSums(values, target):
	dict = {}
	for ind, val in enumerate(values): # 0, 3
		goal = target - val
		if goal in dict:
			return [ind, dict[goal]]
		dict[val] = ind
	# Return an empty list if no solution is found
	return []

			
res = twoSums(values, target)
print('Results: ', res)	

# O(n2) complexity
# def twoSums(values, target):
# 	iterator = len(values)  # 3
# 	for ind, val in enumerate(values):
# 		print(ind, val) # 1, 2
# 		nextind = ind # 0
# 		iterator -= 1 # 2
# 		if ind == len(values) - 1:
# 			print('None passed')
# 			break
	
# 		for i in range(iterator): # 0, 1
# 			nextind += 1 # 1
# 			print('nextind', nextind)
# 			nextval = values[nextind]
# 			sum = val + nextval # 2 + 4 = 6
# 			print('sum', sum) # 5
# 			if sum == target:
# 				print(True, val, nextval)
# 				return [ind, nextind]

# Two passes maybe O(n2)
# def twoSums(values, target):
# 	for ind, val in enumerate(values):
# 		print(ind, val) # 1, 3
# 		goal = target - val
# 		if goal in values:
# 			if goal == val:
# 				allidxs = [i for i, val in enumerate(values) if val == goal]
# 				if len(allidxs) == 2 and ind in allidxs:
# 						return allidxs
# 			else:
# 				return [ind, values.index(goal)]