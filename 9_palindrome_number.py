class Solution:
    def isPalindrome(self, x: int) -> bool:
        # On time, On space
        x = str(x)
        left = 0
        right = len(x) - 1
        while left <= right:
            if x[left] != x[right]:
                return False
            left += 1
            right -= 1

        return True

        # no string conversion
        # On time, O1 space
        if x < 0: # all negatives are not palindromes
            return False
        rev = 0
        num = x
        while num:
            rev = (rev * 10) + (num % 10)
            num = num // 10

        return rev == x
        
