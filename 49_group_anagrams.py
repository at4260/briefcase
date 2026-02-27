
def groupAnagrams(strs: List[str]) -> List[List[str]]:
	# brute force
	# O m x nlogn (sort) time, O(m * n) space

	res = {}
	for s in strs:
		s_sort = ''.join(sorted(s))
		if res.get(s_sort):
			res[s_sort].append(s)
		else:
			res[s_sort] = [s]
	
	# alternative using default dict
	res = defaultdict(list)
	for s in strs:
		s_sort = ''.join(sorted(s))
		res[s_sort].append(s)

	# {aet: [eat,tea,ate], ant: [tan], abt: [bat]}
	return list(res.values())

	# don't sort the strings, sort in tuple hash map
	# # O m x nlogn (sort) time, O(m * n) space
	res = defaultdict(list)
	# {
	#   ((a,1),(e,1),(t,1)): [eat,tea,ate], 
	#   ((a,1),(n,1),(t,1)): [tan], 
	#   ((a,1),(b,1),(t,1)): [bat]
	# }
	for s in strs:
		charset = defaultdict(int)
		for char in s:
			charset[char] += 1
		charset_key = tuple(sorted(charset.items()))
		res[charset_key].append(s)
	
	return list(res.values())

	# don't sort the strings, sort in tuple hash map with all characters
	# # O (m * n) time, O(m * n) space
	res = defaultdict(list)
	# {
	#   (1,0,0,0,1,...,1,0,0...): [eat,tea,ate], 
	#   (1,0,0,0,0,1,.,1,0,0...): [tan], 
	#   (1,1,0,0,0,...,1,0,0...): [bat]
	# }
	for s in strs:
		charset = [0] * 26
		for char in s:
			# ord('a') = 97
			charset[ord(char) - ord('a')] += 1
		charset_key = tuple(charset)
		res[charset_key].append(s)
	
	return list(res.values())        


strs = ["eat","tea","tan","ate","nat","bat"]
# output = [["bat"],["nat","tan"],["ate","eat","tea"]]
res = groupAnagrams(strs)
print('Results: ', res)	
