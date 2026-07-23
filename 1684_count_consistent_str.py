class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # O(n*m) time m = max word length (or O(n) n = total chars across all words), On space
        allowed_set = set(allowed) # On space
        count = 0

        for word in words:
            is_valid = True
            for char in word:
                if char not in allowed_set:
                    is_valid = False
                    break
            if is_valid:
                count += 1

        return count
    