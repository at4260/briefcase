# Given an array of strings, group all strings that belong to the same shifting sequence.
# A shifting sequence is formed by repeatedly shifting letters in a string:
	# Right shift: Replace each letter with the next letter in the alphabet (a→b, b→c, ..., z→a)
	# Left shift: Replace each letter with the previous letter in the alphabet (z←a, b←a, ..., a←z)
	# For example, the strings "abc", "bcd", "xyz", "yza", and "zab" all belong to the same shifting sequence because:

# "abc" can be right-shifted to "bcd"
# "bcd" can be right-shifted multiple times to eventually get "xyz"
# "xyz" can be right-shifted to "yza"
# "yza" can be right-shifted to "zab"
# "zab" can be right-shifted to "abc" (completing the cycle)

# Example 1:

# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
# Example 2:

# Input: strings = ["a"]
# Output: [["a"]]

# Constraints

# 1 <= strings.length <= 200
# 1 <= strings[i].length <= 50
# strings[i] consists of lowercase English letters

from collections import defaultdict
def groupShiftedStrings(strs: list[str]) -> list[list[str]]:
	# wraparound technique is to use %26 and treat a-z like a circle
		# a + 1 = (0 + 1) % 26 = 1 => b
		# b + 1 = (1 + 1) % 26 = 2 => c
		# z + 1 = (25 + 1) % 26 = 0 => a 
		# a - 1 = (0 - 1) % 26 = 25 => z
		# b - 1 = (1 - 1) % 26 = 0 => a
		# z - 1 = (25 - 1) % 26 = 24 => y

	# brute force
	# O(n^2 * m) time, O(n) space; m = chars per string
	# (25, 0): [za], (2,4): [ce]
	# [ab] -> (0,1)
	groups = defaultdict(list)
	for s in strs:
		key = [ord(char) - ord('a') for char in s]
		matched = False

		# shift each key in groups and check it against our curr key for a match
		for group in groups:
			if len(group) != len(key):
				continue
            
			diff = (group[0] - key[0]) % 26
			newgroup = [(val - diff) % 26 for val in group]
			if newgroup == key:
				matched = True
				groups[group].append(s)
				break

		if not matched:
			groups[tuple(key)].append(s)
        
	return list(groups.values())


	# ideal
	# O(n*m) time, O(n) space
	# { (1) : [za, yz, ab] } tuple of distance between each letter
	groups = defaultdict(list)
	for s in strs:
		key = []
		for i in range(len(s)):
			if i != 0:
				position = ord(s[i]) - ord('a')
				old_position = ord(s[i-1]) - ord('a')
				key.append((position - old_position) % 26)

		groups[tuple(key)].append(s)

	return list(groups.values())


strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
output = [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
res = groupShiftedStrings(strings)
print('Results: ', res)	

strings = ["a"]
output = [["a"]]
res = groupShiftedStrings(strings)
print('Results: ', res)	
