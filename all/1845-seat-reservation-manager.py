'''
2023/11/06 daily challenge

min heap approach
'''

import heapq


class SeatManager:

    def __init__(self, n: int):
        # the position of the first unused vacant seat
        self.first_vacant = 1
        # min heap of unreserved seats which were used and then unreserved.
        self.h = []

    def reserve(self) -> int:
        if self.h:
            return heapq.heappop(self.h)
        
        reservation = self.first_vacant
        self.first_vacant += 1
        return reservation

    def unreserve(self, seatNumber: int) -> None:
        heapq.heappush(self.h, seatNumber)

