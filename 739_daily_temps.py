
def dailyTemperatures(temperatures: List[int]) -> List[int]:
	# brute force
	# On2 time, On space
	# answers = [0] * len(temperatures)
	# for i in range(len(temperatures)):
	#     for j in range(i+1, len(temperatures)):
	#         if temperatures[i] < temperatures[j]:
	#             answers[i] = j - i
	#             break

	# return answers

	# stacks solution
	# On time, On space
	stack = [] # store index
	answers = [0] * len(temperatures)

	for i in range(len(temperatures)):
		while stack and temperatures[stack[-1]] < temperatures[i]:
			answers[stack[-1]] = i - stack[-1]
			stack.pop()
		stack.append(i)

	return answers


temperatures = [73,74,75,71,69,72,76,73]
# output [1,1,4,2,1,1,0,0]
res = dailyTemperatures(temperatures)
print('Results: ', res)	
