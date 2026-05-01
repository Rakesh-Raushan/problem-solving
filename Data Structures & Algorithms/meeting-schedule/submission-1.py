"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
            # we need to sort them first on basis of start times
            intervals.sort(key=lambda x: x.start)
            last_meet_end = -1
            for meeting in intervals:
                #check if meeting starts after the last meeting end
                if meeting.start >= last_meet_end:
                    #can schedule
                    last_meet_end = meeting.end
                else:
                    return False
            
            #if we could traverse all meetings, it means there is no conflict
            return True

    #there is a conflict if:
            #a meeting starts before an ongoing meeting is over
            #a meeting ends
            # [(0,30),(5,10),(15,20)] > (0,30), start=end = -1
            # 0>end, end=30, 5>end no so conflict
            # [(5,8),(9,15)]
            #5>-1 so can start, end = 8, 9 >8 so can start, end = 15 no conflict
            #[(9,15), (5,8)], 9>-1, end = 15, 5>15 no so can not start

