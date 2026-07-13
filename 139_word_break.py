class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # time limit exceeded, need memoization approach
        # O(t * m^n) time where t = max length of any word in word dict, m = word dict, n = s
            # at each position in s, you're exploring every word in wordDict and backtracking
        # O(n) space for call stack - one char in s at a time
        
        def substr_match(i):
            if i == len(s):
                return True
        
            for word in wordDict:
                if s[i:i+len(word)] == word:
                    new_i = i + len(word)
                    if substr_match(new_i):
                        return True
            return False

        return substr_match(i=0)        
    
