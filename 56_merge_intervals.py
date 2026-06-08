class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(n log n) time, O(1) space excluding output
        intervals.sort(key=lambda pair: pair[0])

        res = []

        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]

            if res:
                prior_start, prior_end = res.pop()
                if curr_start <= prior_end:
                    res.append([prior_start, max(curr_end, prior_end)])
                else:
                    res.append([prior_start, prior_end])
                    res.append([curr_start, curr_end])
            else:
                res.append([curr_start, curr_end])

        return res


        # [1,3],[2,6],[8,10],[15,18]]
        # [[1,4],[4,7][7,9]]
        # [[1,4]]