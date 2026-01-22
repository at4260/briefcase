# values = [-1,0,1,2,3,7]
values = [2, 3, 3]
target = 6


def twoSums(numbers, target):
	left, right = 0, len(numbers) - 1
	# for i in range(len(numbers)):
	while left < right:
		if numbers[left] + numbers[right] == target:
			return [left + 1, right + 1]
		elif numbers[left] + numbers[right] > target:
			right -= 1
		elif numbers[left] + numbers[right] < target:
			left += 1
	
	return []

			
res = twoSums(values, target)
print('Results: ', res)	
