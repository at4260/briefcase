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

# valid palindrome using an int and constant space
class Solution:
    def is_palindrome(self, input_int: int) -> bool:
        """
        Returns true if the input integer is a palindrome
        with constant space complexity.
        :param input_int: Input integer to be tested.
        :return: True if the input integer is a palindrome.
        """

        # reverse the int arithmetically and compare results
        copy_int = input_int
        reversed_int = 0
        while copy_int: 
            remainder = copy_int % 10
            reversed_int = reversed_int * 10 + remainder
            copy_int = copy_int // 10
            
        return reversed_int == input_int
            