class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        # fails on rick -> kric, order matters
        # typed_count = defaultdict(int)
        # for char in typed:
        #     typed_count[char] += 1

        # for char in name:
        #     if typed_count[char] == 0:
        #         return False
        #     typed_count[char] -= 1

        # return True

        # O(n+m) time, O(1) space
        name_i = 0
        typed_i = 0

        while name_i < len(name):
            # case: extra name chars; name = alexy, typed = aaleex
            if typed_i >= len(typed):
                return False
            # case: mismatched letters; name = rick, typed = kric
            if name[name_i] != typed[typed_i]:
                return False
            # case: typed char count >= name char count; name = leelee, typed = lleeelee
            name_count, typed_count = 1, 1
            while name_i < len(name) - 1 and name[name_i] == name[name_i + 1]:
                name_count += 1
                name_i += 1
            while typed_i < len(typed) - 1 and typed[typed_i] == typed[typed_i + 1]:
                typed_count += 1
                typed_i += 1
            if typed_count < name_count:
                return False

            name_i += 1
            typed_i += 1

        # case: extra typed chars; name = alex, typed = aaleexy
        return typed_i == len(typed)

        # better
        i, j = 0, 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j] == typed[j - 1]:
                j += 1
            else:
                return False
        return i == len(name)