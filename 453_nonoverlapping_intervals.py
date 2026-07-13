class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # [1,4][3,5][4,6] -> remove 1 [3,5]
        # O(n log n) time for sort, O(n) for res

        intervals.sort(key=lambda pair: pair[0])

        res = []
        for interval in intervals:
            if not res:
                res.append(interval)
            else:
                prev_start, prev_end = res[-1]
                curr_start, curr_end = interval

                if curr_start < prev_end: # overlap
                    prev_interval = res.pop()
                    earliest_end = prev_interval if prev_end < curr_end else interval
                    res.append(earliest_end)
                else:
                    res.append(interval)

        return len(intervals) - len(res)
            