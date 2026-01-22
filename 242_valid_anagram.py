def test_func(s: str, t: str) -> bool:
	# O(n log n) time complexity due to sorting
	# O(n) space complexity
	# s1 = list(s)
	# t1 = list(t)
	# s1.sort()
	# t1.sort()
	# print(s1)
	# print(t1)
	# return s1 == t1
	
	# O(n) time complexity 
	# O(n) space complexity
	# if len(s) != len(t):
	# 	return False
	
	# s_seen = {}
	# for x in s:
	# 	if x in s_seen:
	# 		s_seen[x] += 1
	# 	else:
	# 		s_seen[x] = 1
	# alternative:
	# for x in s:
	# 	s_seen[x] = s_seen.get(x, 0) + 1

	# for y in t:
	# 	if y not in s_seen:
	# 		return False
	# 	else:
	# 		s_seen[y] -= 1
	# 		if s_seen[y] == 0:
	# 			s_seen.pop(y)

	# return True
    

	# O(n2) time complexity due to replace doing another scan of the string
	# O(n) space complexity due to creating new string each time
	if len(s) != len(t):
		return False

	for x in s:
		print(1, x, s, t)
		if x in t:
			t = t.replace(x, '', 1)
		else:
			return False

	return True	


		


s = "aacc"
# t = "arttt"
t = "ccac"
res = test_func(s, t)
print('Results: ', res)	
