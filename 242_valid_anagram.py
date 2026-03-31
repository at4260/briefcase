def test_func(s: str, t: str) -> bool:
	# O(n log n) time complexity due to sorting
	# O(n) space complexity
	# s1 = sorted(s)
	# t1 = sorted(t)
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

	seen = defaultdict(int)
	for char in s:
		seen[char] += 1

	for char in t:
		if seen.get(char):
			seen[char] -= 1
			if not seen[char]:
				seen.pop(char)
		else:
			return False

	return not seen 
		


s = "aacc"
# t = "arttt"
t = "ccac"
res = test_func(s, t)
print('Results: ', res)	
