class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # O(n) time, O(n) space
        mid = len(s) // 2 # len = 4, mid = 2
        vowel_set = set("aeiouAEIOU")
        
        count_a = sum(1 for char in s[:mid] if char in vowel_set) # O1 lookup
        count_b = sum(1 for char in s[mid:] if char in vowel_set)        
        return count_a == count_b