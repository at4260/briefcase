from collections import deque

def countStudents(students: List[int], sandwiches: List[int]) -> int:
	# brute force 
	# O(n2) time, O(1) space
	# students = deque(students)
	# sandwiches = deque(sandwiches)

	# reset = 0
	# remaining = len(students)
	# while reset < remaining: 
	#     if students[0] == sandwiches[0]:
	#         students.popleft()
	#         sandwiches.popleft()
	#         reset = 0
	#         remaining = len(students)
	#     else:
	#         students.append(students.popleft()) # move front to back
	#         reset += 1

	# return len(students)


	# optimal
	# On time, O1 space
	# insight: student order doesn't matter because it can keep rotating; sandwich order matters
	res = len(students)
	count = {0: 0, 1: 0}
	for s in students:
		count[s] += 1

	for s in sandwiches:
		if count[s] > 0:
			count[s] -= 1
			res -= 1
		else:
			break

	return res




students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
# output = 3
res = countStudents(students, sandwiches)
print('Results: ', res)	
