def test_func(nums1: list, m: int, nums2: list, n: int) -> None:
	# return nothing, modify nums1 in place

	# brute force
	# chop off the end elements, slap nums2 in, and then sort
	# O nlog n time
	# O 1 space
	# nums1[m:] = nums2
	# return nums1.sort()

	# pointers
	# O1 space, On+m time
	idx1 = m - 1 # largest value for nums1
	idx2 = n - 1 # largest value for nums2
	pointer = len(nums1) - 1
	# pop largest value in to replace the 0 spaceholders at the end
	while idx1 >=0 and idx2 >= 0 and pointer >= 0:
		if nums1[idx1] > nums2[idx2]:
			nums1[pointer] = nums1[idx1]
			pointer -= 1 
			idx1 -= 1 

		elif nums1[idx1] <= nums2[idx2]:                
			nums1[pointer] = nums2[idx2]
			pointer -= 1
			idx2 -= 1  

	# edge case when there are nums2 values smaller than nums1[0]
	while idx2 >= 0 and pointer >= 0:
		nums1[pointer] = nums2[idx2]
		pointer -= 1
		idx2 -= 1  


	# simplified of above
	# keep processing nums2 until we have put all the values into nums1
	# while idx2 >= 0 and pointer >= 0:
	#     if idx1 >= 0 and nums1[idx1] > nums2[idx2]:
	#         nums1[pointer] = nums1[idx1]
	#         pointer -= 1 
	#         idx1 -= 1 

	#     else:
	#         nums1[pointer] = nums2[idx2]
	#         pointer -= 1
	#         idx2 -= 1               

	return nums1


s = [1,2,5,3,4,5]			
res = test_func(s)
print('Results: ', res)	
