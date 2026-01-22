import re
s = "A man, a plan, a canal: Panama"
# s = "race a car"
s = ""


def isPalindrome(s):
	# clean our string
    s = s.lower()
    str = re.sub(r'[^a-zA-Z0-9]', '', s)
    # s = "amanaplanacanalpanama"

    # brute force - copy, reverse, compare
    # return str == str[::-1]
    # on space
    # on time


    # edge cases
    # s = "" -> true
    # s = "a" -> true
    # s = "aa" -> true midpoint = 1
    # s = "aba" -> true midpoint = 1
    # s = "racr" -> true midpoint = 1
    # s = "racar" -> true midpoint = 1

    # two pointers
    left, right = 0, len(str) - 1
    midpoint = len(str) // 2
    for i in range(0, midpoint):
    # alternative: while left < right:
        if str[left] != str[right]:
            return False
        left += 1
        right -= 1
    return True
    # O1 space
    # On time



			
res = isPalindrome(str)
print('Results: ', res)	
