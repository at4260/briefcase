
def evalRPN(tokens: List[str]) -> int:
	# O(n) time, O(n) space
	stack = []

	for token in tokens:
		if token in ['+', '-', '*']:
			res = eval(f"{stack[-2]} {token} {stack[-1]}")
			stack.pop()
			stack.pop()
			stack.append(int(res))
		elif token == '/':
			res = int(stack[-2] / stack[-1]) # truncate to 0
			stack.pop()
			stack.pop()
			stack.append(int(res))
		else:
			stack.append(int(token))

	return stack[-1]


tokens = ["4","13","5","/","+"] # res = 6
# (4 + (13 / 5)) = 6
res = evalRPN(tokens)
print('Results: ', res)	
