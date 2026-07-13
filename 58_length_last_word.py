class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # O(n) time, O(n) space
        # s = s.strip()
        # s = s.split(" ")
        # last_word = s[-1]

        # return len(last_word)

        # O(n) time, O(1) space
        res = 0
        for i in range(len(s) - 1, -1, -1): # iterate backwards
            if s[i] != " ":
                res += 1
            else: # hits a blank
                if res:
                    return res

        return res
