class Solution:
    # O(n+m) time, n = list of strs, m = char in str, going through the list in one pass through each char
    # O(n+m) space
    def encode(self, strs: List[str]) -> str:
        # encode by putting [length of str]#[str], ex: "3#bad4#####10#1234567890"
        # the "#" tells us where the length number ends since only the length is variable
        res = ""
        for s in strs:
            encoded_s = str(len(s)) + "#" + s
            res += encoded_s

        return res

        # more optimal to use join since res += encoded_s reassigns a new var each time
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append("#")
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # loop through until you hit a "#" to stop tracking the size
        res = []
        size = ""
        i = 0
        while i < len(s):
            if s[i] != "#":
                size = str(size) + str(s[i])
                i += 1
            elif s[i] == "#":
                size = int(size)
                res.append(s[i+1:(i + 1 + size)])
                # reset everything
                i += 1 + size
                size = ""

        return res
