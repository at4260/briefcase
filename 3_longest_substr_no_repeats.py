

def lengthOfLongestSubstring(s: str) -> int:
	# Test cases
	# s = "" => 0 
	# s = "a" => 1
	# s = "aa" => 1
	# s = "ab" => 2
	# s = "abbb" => 2
	# s = "aaab" => 2
	# s = "acaab" => 2

	# brute force - check all possibilities
	# On2 time, O(n) space since allows letters, digits, spaces
		# spaces can still be keys in dict
	# max_len = 0
	# for left in range(len(s)):
	#     seen = {} # char: freq, optimally convert to a set instead
	#     for right in range(left, len(s)):
	#         if s[right] in seen:
	#             break
	#         else:
	#             seen[s[right]] = 1
	#             max_len = max(right - left + 1, max_len)

	# return max_len

	# optimal - sliding window
	# On time, O(n) space 
	max_len = 0
	seen = {} # char: freq 
	left = 0
	for right in range(len(s)):
		while s[right] in seen:
			del seen[s[left]]
			left += 1
		seen[s[right]] = 1
		max_len = max(right - left + 1, max_len)

	return max_len

	# more optimal
	# seen = {} char: index of occurrence
	# use the index to jump the left pointer to seen[left] + 1 to avoid having 
	# to keep moving the left pointer while we find a valid substring (can get
	# rid of the while loop)
	# max_len = 0
	# seen = {} # char: index 
	# left = 0
	# for right in range(len(s)):
	# 	if s[right] in seen:
	#		left = max(seen[s[right]] + 1, left) # never move left backwards since i'm not reupdating or removing old seen indexes
	# 	seen[s[right]] = right
	# 	max_len = max(right - left + 1, max_len)

	# return max_len



s = "pwwkew" # => 3
res = lengthOfLongestSubstring(s)
print('Results: ', res)	
