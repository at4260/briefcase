
def searchMatrix(matrix: List[List[int]], target: int) -> bool:
	# Test cases
	# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3 => true
	# matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13 => false
	# matrix = [[1]], target = 1 => true
    # matrix = [[1]], target = 0 => false

	# brute force - search through entire matrix
	# O(m * n) space (O(n2)), O1 space
	# for i in range(0, len(matrix)):
	# 	for j in range(0, len(matrix[i])):
	# 		if matrix[i][j] == target:
	# 			return True
	# return False

	# optimal - binary search
	# O log n time, O1 space
	# treat it like a 1d array without actually converting it
    
	m = len(matrix) # row
	n = len(matrix[0]) # col
	left, right = 0, (m * n) - 1

	while left <= right:
		mid = (left + right) // 2
	    # translate mid to 2d
		row_idx = mid // n
		col_idx = mid % n

		if matrix[row_idx][col_idx] == target:
			return True
		elif matrix[row_idx][col_idx] < target:
			left = mid + 1
		else: # matrix[row_idx][col_idx] > target:
			right = mid - 1

	return False


matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
res = searchMatrix(matrix, target)
print('Results: ', res)	
