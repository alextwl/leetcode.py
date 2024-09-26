'''
2022/08/03 daily challenge

brute force checking just like problem 2446.
'''

class MyCalendar:

    def __init__(self):
        self.bookings = []  # list of scheduled bookings.

    def book(self, start: int, end: int) -> bool:
        for bStart, bEnd in self.bookings:
            # note the end time is not inclusive.
            if bStart < end and start < bEnd:
                # conflict found.
                return False
        # booking succeeded.
        self.bookings.append((start, end))
        return True


'''
SortedList approach, learnt from official solution 2.

sort the bookings and find the conflict by binary search provided by SortedList.
'''

from sortedcontainers import SortedList


class MyCalendar:

    def __init__(self):
        self.bookings = SortedList()  # list of scheduled bookings.

    def book(self, start: int, end: int) -> bool:
        '''
        find a proper index of the incoming request to be inserted where
        next to a scheduled booking [bStart, bEnd) by bStart > start.
        '''
        idx = self.bookings.bisect_right((start, end))
        '''
        (1) if idx > 0, lookup the previous booking of idx (that is, bookings[idx-1])
            and check if its end time is later than start.
        (2) check if the start time of the bookings[idx] was earlier than the incoming end time.
        '''
        if (idx > 0 and self.bookings[idx-1][1] > start) or \
            (idx < len(self.bookings) and self.bookings[idx][0] < end):
            return False
        # conflict not found, good to accept booking.
        self.bookings.add((start, end))
        return True


'''
manual insort_right ver
'''


import bisect


class MyCalendar:
    def __init__(self):
        self.reservations = []

    def book(self, start: int, end: int) -> bool:
        i = bisect.bisect_right(self.reservations, (start, end))
        if i > 0 and self.reservations[i-1][1] > start:
            return False
        if i < len(self.reservations) and end > self.reservations[i][0]:
            return False
        self.reservations.insert(i, (start, end))
        return True

