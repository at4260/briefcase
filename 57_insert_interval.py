class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        # option 1: sort by start including newInterval, then loop through and merge intervals
        # O(nlogn) time, O(1) space excluding output arr

        intervals.append(newInterval)
        intervals.sort(key=lambda pair: pair[0])

        res = []
        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]
            if not res:
                res.append([curr_start, curr_end])
            else:
                prev_start, prev_end = res[-1]
                if curr_start <= prev_end:
                    res.pop()
                    res.append([min(curr_start, prev_start), max(curr_end, prev_end)])
                else:
                    res.append([curr_start, curr_end])

        return res

        # option 2: loop through comparing current value to new interval and determining merge
        # O(n) time, O(1) space excluding output arr

        # [[3,5], [6,8], [12,14]]

        # new = [1,2] # new gets inserted first, then curr
        #     - done
            
        # new = [2,6] # one insert as a merge
        #     - no res, [2,6]

        # new = [8,15] # one insert as a merge

        # new = [9,10] # new slot

        # new = [16,18] # curr inserted, then new

        res = []
        for i in range(len(intervals)):
            curr_start, curr_end = intervals[i]
            new_start, new_end = newInterval
            
            if new_end < curr_start: # no overlap, new before intervals[i]
                res.append([new_start, new_end])
                return res + intervals[i:]
            elif curr_end < new_start: # no overlap, new after intervals[i]
                res.append([curr_start, curr_end])            
            elif max(curr_start, new_start) <= min(curr_end, new_end): # overlap
                newInterval = [min(curr_start, new_start), max(curr_end, new_end)]

        res.append(newInterval)
        return res


