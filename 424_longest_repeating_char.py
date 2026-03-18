
def characterReplacement(s: str, k: int) -> int:
	# brute force - checks every possibility while keeping a dict to increment counts
	# saves max length only when the condition is met
	# On2 time, O1 space (specifically O(26))
	# max_len = 1
	# for i, char in enumerate(s):
	#     seen = {} # char: freq
	#     seen[char] = seen.get(char, 0) + 1 
	#     # could also set max_len = 0 and use `for j in range(i, len(s))`
	#     for j in range(i+1, len(s)):    
	#         seen[s[j]] = seen.get(s[j], 0) + 1
	#         # max_char = max(seen, key=seen.get) # get key for max val
	#         max_count = max(seen.values()) # get max val
	#         curr_len = j - i + 1
	#         if (curr_len - max_count) <= k:
	#             max_len = max(max_len, curr_len)

	# return max_len


	# sliding window - smartly moves the window along to only check valid possibilities
	# aka as soon as a window is no longer valid, there's no need to continue expanding 
	# the right pointer window to keep checking

	# O(n) time for the loop * O(26) time for the occasional maxf lookup => O(n * 26) => O(n), 
	# O(1) space (specifically O(26))	
	i, j = 0, 0
	count = {}
	maxf = 0
	res = 0
	while j < len(s):
		count[s[j]] = count.get(s[j], 0) + 1
		maxf = max(count.values())
		sublen = j - i + 1
		if (sublen - maxf) <= k: # valid
			res = max(res, sublen)
		else:
			count[s[i]] -= 1
			maxf = max(count.values()) # updates maxf - this version doesn't include the stale maxf trick (see Note 2)
			i += 1
		j += 1

	return res


	# O(n) time, O(1) space (specifically O(26))
	max_len = 0
	i = 0
	seen = {} # char: freq
	for j in range(len(s)):
		seen[s[j]] = seen.get(s[j], 0) + 1
		max_count = max(max_count, seen[s[j]]) # O(1) time
		curr_len = j - i + 1
		# while loop is canonical here, see note 1 below
		if (curr_len - max_count) <= k:
			max_len = max(max_len, curr_len)
		else:
			seen[s[i]] -= 1  # decrement seen to remove val
			i += 1

	return max_len


s = "ABBB"
k = 0			
res = characterReplacement(s, k)
print('Results: ', res)	


'''
Note 1: If a substring works, and I'm now moving my right pointer to expand the window, 
and now the substring is invalid, then there's no point moving solely just the left pointer,
which is what the while loop version does.

This is because best case, moving the left pointer makes the substring valid but now has 
the same max length of the previous substring that worked, and worse case, it's invalid 
and I have to move the right pointer anyways, so might as well just move it now.

My logic:
Window is valid at length N
Expand right → now invalid at length N+1
If I shrink left, best case: valid at length N (which I already have!)
So skip directly to: shrink left once AND expand right

Why this works:
You're never going to beat max_len by checking windows shorter than what you've already found
The only way to beat max_len is to find a LONGER valid window
So when invalid, just shift the window forward (both pointers move) rather than exhaustively checking all shorter subwindows

The standard while loop approach:
Shrinks until valid, THEN expands
Checks more windows explicitly
More intuitive to explain ("keep shrinking until valid")
'''

'''
Note 2: Optimal stale max_count solution:

	max_len = 0
	max_count = 0
	i = 0
	seen = {} # char: freq

	for j in range(len(s)):
		seen[s[j]] = seen.get(s[j], 0) + 1
		max_count = max(max_count, seen[s[j]])
		while (j - i + 1) - max_count > k: # curr length minus max count
			seen[s[i]] -= 1  # decrement seen to remove val
			i += 1
		max_len = max(max_len, j - i + 1)

	return max_len

The idea behind this is that if ex: length = 5 and max_count = 3 and k =2 is valid, then when any length is of 5 or less, 
I don't care whether max_count has been updated or not (stale) because the best case is it's valid and the max length 
is still 5, worst case is now it's invalid. 
If I'm looking at a length greater than 5, then I do care because if I want to maximize length then I also need to 
maximize max_count to keep the total at 2 and under. 

The insight:
Once we've found a valid window of length N, we only care about finding windows of length > N
For any window of length ≤ N, it doesn't matter if it's valid or not - it can't beat our current best
For windows of length > N, we need the TRUE max_count to accurately determine validity
But: max_count only increases (when we add new characters), it never decreases in the code 
So when we find a NEW character that increases max_count, we're using the correct updated value for that longer window
The staleness only affects our decision about SHORTER windows (which we don't care about anyway)

So the stale max_count is "harmless" because:
It might make us keep a window that's actually invalid, but that window is ≤ our previous best anyway
When we expand to a NEW longest window, we update max_count correctly (when we see a new max frequency character)

* Additional key insight: If we find a window of length N that's valid and then hit an invalid window of N+1, we
don't bother shrinking the window to try to find a valid window of length N again, because we already have that 
length as our best result. So we keep the N+1 window size and keep sliding forward, while only expanding, never shrinking.

Summary: We never need to recalculate maxf when shrinking because we only care about beating our current best result. 
To find a longer valid window, maxf would need to legitimately grow anyway — and it only grows when we expand j and 
find a real character count increase. So a stale maxf might let us slide the window without shrinking, but it can never 
produce a false best result.

'''
