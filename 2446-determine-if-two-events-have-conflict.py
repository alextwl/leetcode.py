'''
since there's constraints all date ranges do not have a span of 2 days,
just convert the HH:MM to integer HHMM and check its intersections.
'''

class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def time2int(strTime: str) -> int:
            return int(''.join(strTime.split(':')))
        
        start1, end1 = map(time2int, event1)
        start2, end2 = map(time2int, event2)
        
        if (start2 <= start1 <= end2) or \
           (start2 <= end1 <= end2) or \
           (start1 <= start2 <= end1) or \
           (start1 <= end2 <= end1):
            return True
        
        return False
