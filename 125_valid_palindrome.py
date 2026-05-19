import re
s = "A man, a plan, a canal: Panama"
# s = "race a car"
s = ""


def isPalindrome(s):
    # O(n) time, O(n) space to clean the string
	# clean our string
    s = s.lower()
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s)
    # s = "amanaplanacanalpanama"

    # brute force - copy, reverse, compare
    # return cleaned == cleaned[::-1]
    # on space
    # on time

    # two pointers
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True

    # O(n) time, O(1) space
    left, right = 0, len(s) - 1
    while left < right:
        while left < right and not isAlphaNum(s[left].lower()):
            left += 1
        while left < right and not isAlphaNum(s[right].lower()):
            right -= 1
        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True

    def isAlphaNum(char):
        # ignore special chars and spaces, only accept letters and numbers
        return (ord('a') <= ord(char) <= ord('z')) or (ord('0') <= ord(char) <= ord('9'))

	
res = isPalindrome(s)
print('Results: ', res)	
