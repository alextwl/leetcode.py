'''
2024/09/27 daily challenge

brute force approach

use two lists to track both reservations & overlapped bookings,
and check overlaps one by one.
'''


class MyCalendarTwo:
    def __init__(self):
        self.resv = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for start2, end2 in self.overlaps:
            if max(start, start2) < min(end, end2):
                return False

        for start2, end2 in self.resv:
            max_start, min_end = max(start, start2), min(end, end2)
            if max_start < min_end:
                self.overlaps.append((max_start, min_end))

        self.resv.append((start, end))

        return True

