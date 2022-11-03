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

