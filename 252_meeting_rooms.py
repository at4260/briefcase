"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # brute force - On^2 time, O1 space
        # for i in range(len(intervals)):
        #     for j in range(i+1, len(intervals)):
        #         s1, e1 = intervals[i].start, intervals[i].end
        #         s2, e2 = intervals[j].start, intervals[j].end
        #         if max(s1, s2) < min(e1, e2): # max of the later meeting needs to be after the min of the earliest meeting
        #             return False

        # return True


        # # sorting - Onlogn time, O1 space
        intervals.sort(key=lambda i: i.start)
        for i in range(len(intervals) - 1):
            s1, e1 = intervals[i].start, intervals[i].end
            s2, e2 = intervals[i+1].start, intervals[i+1].end
            if s2 < e1:
                return False

        return True