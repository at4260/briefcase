class Solution:
    def makeGood(self, s: str) -> str:
        # On space, On time
        stack = []
        for char in s:
            if not stack:
                stack.append(char)
            else:
                last_char = stack.pop()
                # char_match = last_char.lower() == char.lower()
                # is_bad = (last_char.isupper() and char.islower()) or (last_char.islower() and char.isupper()) 
                # if not char_match or not is_bad:

                # ee, -> true, ab -> true, eE -> false
                if not (last_char != char and last_char.lower() == char.lower()): # exclude: not the same char but same lowercase letter
                    stack.append(last_char)
                    stack.append(char)

        return "".join(stack)
