
def threeSum(nums: list) -> list[int]:
    # brute force
    # On3 time, On space
	# triplets = []
	# nums.sort()
	# for i in range(len(nums) - 2):
	# 	for j in range(i + 1, len(nums) - 1):
	# 		for k in range(i + 2, len(nums)):
	# 			if nums[i] + nums[j] + nums[k] == 0:
	# 				found = [nums[i], nums[j], nums[k]]
	# 				if found not in triplets:
	# 					triplets.append(found)

	# return triplets

    # another option
    # on3 time, on space
	# triplets = []
	# nums.sort() # [-4,-1,-1,0,1,2]
	# for i in range(len(nums)): # O(n) time
	# 	left = i + 1
	# 	right = len(nums) - 1
	# 	while left < right: # O(n) time
	# 		if nums[left - 1] == nums[left]:
	# 			left += 1
	# 		if right < len(nums) - 1 and nums[right + 1] == nums[right]:
	# 			right -= 1
				
	# 		total = nums[i] + nums[left] + nums[right]				
	# 		if total > 0:
	# 			right -= 1
	# 		elif total < 0:
	# 			left += 1
	# 		else: 
	# 			found = [nums[i], nums[left], nums[right]]
	# 			if found not in triplets: # O(n) each check, not ideal
	# 				triplets.append(found)
	# 			right -= 1
	# 			left += 1

	# return triplets

	# ideal
    # on2 time, on space
	# triplets = []
	# nums.sort() # [-4,-1,-1,0,1,2]
	# for i in range(len(nums)):

	# 	# don't reevalute the exact same value since we already found the match, ex: [-3,-3,-3,6]
	# 	# we would find [-3,-3,6] (0,1,3) the first time so we don't need to check -3 at index 1 
	# 	# only to find the same [-3,-3,6] (1,2,3) combo
	# 	if i > 0 and nums[i] == nums[i - 1]:
	# 		continue # skip

	# 	left = i + 1
	# 	right = len(nums) - 1
	# 	while left < right:
	# 		# skip all left duplicates, the value before was already evaluated so need to evaluate it again
	# 		# but ensure we aren't comparing it to i since that's the first left position (not a dupe) ex [-1,-1,0,0,2]
	# 		while left - 1 != i and left < right and nums[left - 1] == nums[left]:
	# 			left += 1
	# 		# ensure right + 1 is a valid index
	# 		while right < len(nums) - 1 and left < right and nums[right + 1] == nums[right]:
	# 			right -= 1

	# 		if left >= right:
	# 			break

	# 		total = nums[i] + nums[left] + nums[right]				
	# 		if total > 0:
	# 			right -= 1
	# 		elif total < 0:
	# 			left += 1
	# 		else: 
	# 			triplets.append([nums[i], nums[left], nums[right]])
	# 			right -= 1
	# 			left += 1

	# return triplets

	# for simplicity:
	# solution is to check dupes on the left and right pointers only AFTER we have found a sum 0 set
	# even though that's inconsistent with how we are proactively checking for dupes on i even
	# if we didn't find a sum 0 set -> AGH! it feels like we should always proactively check for dupes
	# if it's something we already evaluated, but it's more prone to edge cases

	triplets = []
	nums.sort() # [-4,-1,-1,0,1,2]
	for i in range(len(nums)):

		# don't reevalute the exact same value since we already found the match, ex: [-3,-3,-3,6]
		# we would find [-3,-3,6] (0,1,3) the first time so we don't need to check -3 at index 1 
		# only to find the same [-3,-3,6] (1,2,3) combo
		if i > 0 and nums[i] == nums[i - 1]:
			continue # skip

		left = i + 1
		right = len(nums) - 1
		while left < right:
			total = nums[i] + nums[left] + nums[right]				
			if total > 0:
				right -= 1
			elif total < 0:
				left += 1
			else: 
				triplets.append([nums[i], nums[left], nums[right]])
				left += 1
				right -= 1

				# skip all the dupes
				while left < right and nums[left - 1] == nums[left]:
					left += 1

				while left < right and nums[right + 1] == nums[right]:
					right -= 1
					

	return triplets	


    


# nums = [-1,0,1,2,-1,-4]
nums = [-1, -1, 0, 0, 0, 1, 1]
res = threeSum(nums)
print('Results: ', res)	
# res = [[-1,-1,2],[-1,0,1]]