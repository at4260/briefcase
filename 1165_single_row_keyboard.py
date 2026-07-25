class Solution:
    def calculate_time(self, keyboard: str, word: str) -> int:
        """
        Calculates the total time needed to type a word on a single-row keyboard.
        
        :param str keyboard: The layout of the keyboard with 26 unique lowercase letters.
        :param str word: The word to type.
        :return: Total time to type the word.
        :rtype: int
        """
        
        # keyboard = "abcdefghijklmnopqrstuvwxyz"
        # word = "cba"
        # pre - 0, c - 2 = > 2- 0 = 2 time
        # pre - 2, b - 1 => abs(1-2) = 1 time
        # pre - 1, a - 0 => abs(0-1) = 1 time
        # sum = 4 time


        # on time, o1 space (constrained by O(26)
        kb_map = {}
        for i, char in enumerate(keyboard):
            kb_map[char] = i
            
        print(kb_map)
        
        total_time = 0
        prev_char_idx = 0
        for char in word:
            idx = kb_map[char]            
            total_time += abs(idx - prev_char_idx)            
            prev_char_idx = idx
            
        return total_time
        