class Solution:
    def minDeletions(self, s: str) -> int:
        # O(26) -> O(1) space for counts_map and sorted values (O(26 log 26))
        # O(26) -> O(1) time, loops array of max size 26, even with lookaheads still bounded by array size
        # aab: {a:2, b:1} [2,1]
        # aaabbbcc: {a:3, b:3, c:2} => delete 2 chars {a:3, b:1, c:2} [3,3,2]
        # ceabaacb: {c:2,e:1,a:3,b:2} [3,2,2,1] => [3,2,1,0]
        # [1,1,1] => [1,0,0]
        # [3,3,3,2,2] => [3,2,1,0,0]
        # [2] => [2]
        # [1,1] => [1,0]

        counts_map = defaultdict(int)
        for char in s:
            counts_map[char] += 1
        # don't care about the letters themselves
        # sort in reverse since we're decrementing counts
        counts = sorted(counts_map.values(), reverse=True)

        deletions = 0
        for i, count in enumerate(counts):
            if count == 0:
                break

            j = i + 1
            while j < len(counts) and counts[j] == count:
                counts[j] -= 1
                deletions += 1
                j += 1

        return deletions


        # seen set approach
        from collections import Counter

        counts = Counter(s)
        seen = set()
        deletions = 0

        for count in counts.values():
            while count > 0 and count in seen:
                count -= 1
                deletions += 1
            if count > 0:
                seen.add(count)

        return deletions
    