class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        # On *m time, m = length of sentence or O(n) where n = total num of words, On space
        max_count = 0
        for sentence in sentences:
            word_count = len(sentence.split(" "))
            max_count = max(max_count, word_count)
        return max_count
        