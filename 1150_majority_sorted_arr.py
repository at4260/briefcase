        # Ologn time, O1 space
		# binary search for leftmost target
		left_idx = None
		left, right = 0, len(arr) - 1 
		while left <= right:
			mid = (left + right) // 2
			if arr[mid] < target:
				left = mid + 1
			elif arr[mid] > target:
				right = mid - 1 
			else:
				left_idx = mid
				right = mid - 1

		right_idx = None
		left, right = 0, len(arr) - 1
		while left <= right:
			mid = (left + right) // 2
			if arr[mid] < target:
				left = mid + 1
			elif arr[mid] > target:
				right = mid - 1 
			else:
				right_idx = mid
				left = mid + 1

		if not right_idx or not left_idx:
			return False
        return (right_idx - left_idx + 1) > len(arr) // 2
