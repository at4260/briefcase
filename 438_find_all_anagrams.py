class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # O(n + m) time with m being length of p (scount == pcount comparison is O(1) because it's bounded by 26 letters), O(1) space (O(26) dict specifically)
        # result = []

        # pcount = defaultdict(int)
        # for char in p:
        #     pcount[char] += 1
        # # pcount = {a:1, b: 1, c:1}

        # left, right = 0, 0
        # scount = defaultdict(int)
        # while right < len(s):
        #     scount[s[right]] += 1
            
        #     if right < len(p) - 1: # setup the initial window
        #         right += 1
        #         continue
        #     if scount == pcount:
        #         result.append(left)
            
        #     # advance the window
        #     scount[s[left]] -= 1
        #     if scount[s[left]] == 0:
        #         del scount[s[left]]
        #     left += 1
        #     right += 1
            
        # return result

        # optimal - doesn't compare pcount to scount every time
        # track if each letter's count matches
        # O(n + m) time with m being length of p, O(1) space (O(26) array specifically)
        result = []
        pcount = [0] * 26
        for char in p:
            pcount[ord(char)-ord('a')] += 1

        scount = [0] * 26
        left, right = 0,0
        matches = sum(1 for i in range(26) if pcount[i] == scount[i])
        while right < len(s):
            scount[ord(s[right])-ord('a')] += 1
            if scount[ord(s[right])-ord('a')] == pcount[ord(s[right])-ord('a')]:
                matches += 1

            if right < len(p) - 1:
                right += 1
                continue
            if matches == 26:
                result.append(left)

            if scount[ord(s[left])-ord('a')] == pcount[ord(s[left])-ord('a')]:
                matches -= 1
            scount[ord(s[left])-ord('a')] -= 1
            left += 1
            right += 1

        return result
    
# Input: s = "cbaebabacd", p = "abc", pcount = {a:1, b:1, c:1}, scount = {c:1, b:1, a:1}; left = 7, right = 10 (len = 10)
# Output: [0,6]
# Input: s = "ccaebabacd", p = "abc"
# Output: [6]
# Input: s = "abab", p = "ab"
# Output: [0,1,2]
