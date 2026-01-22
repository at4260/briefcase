def isValid(s: str) -> bool:
	seen_brackets = []
	open_brackets = ["(", "[", "{"]
	closed_brackets = [")", "]", "}"]
	bracket_match = {")": "(", "]": "[", "}": "{"}
	# ()

	for bracket in s:
		if bracket in open_brackets:
			seen_brackets.append(bracket)
		elif bracket in closed_brackets:
			if seen_brackets and seen_brackets[-1] == bracket_match[bracket]:
				seen_brackets.pop(-1)
			else:
				return False
			
	# 		if seen_brackets and seen_brackets[-1] == bracket_match[bracket]:
	# 			seen_brackets.pop(-1)
	# 		else:
	# 			return False

	# 	else:
	# 		return False			

	# return True if len(seen_brackets) == 0 else False
	return len(seen_brackets) == 0 
        
s = "()"
s = "(())"
s = "("
s = ")"
s = "(()"
s = "())"

s = "([])"			
res = isValid(s)
print('Results: ', res)	

	# cleaned up conditionals
	# for bracket in s:
	# 	if bracket in open_brackets:
	# 		seen_brackets.append(bracket)
	# 	elif bracket in closed_brackets:
	# 		print(1, seen_brackets)
	# 		if seen_brackets and seen_brackets[-1] == bracket_match[bracket]:
	# 			seen_brackets.pop(-1)
	# 		else:
	# 			return False
	# 	else:
	# 		return False

	# print(2, seen_brackets)
	# if len(seen_brackets) == 0:
	# 	return True
	# else:
	# 	return False