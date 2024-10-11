'''
2024/10/11 daily challenge

simulation + min heap approach
'''


import heapq


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        t_arrival, _ = times[targetFriend]
        # filter frields later than the target out
        times = [(x, y, i) for i, (x, y) in enumerate(times) if x < t_arrival]
        times.sort()
        
        occupied_seats = []  # (leaving, seat_num)
        vacant_seats = []  # seat_num
        last_seat_num = 0

        for arrival, leaving, i in times:
            while occupied_seats and occupied_seats[0][0] <= arrival:
                _, released_seat = heapq.heappop(occupied_seats)
                heapq.heappush(vacant_seats, released_seat)

            if not vacant_seats:
                heapq.heappush(occupied_seats, (leaving, last_seat_num))
                last_seat_num += 1
            else:
                heapq.heappush(occupied_seats, (leaving, heapq.heappop(vacant_seats)))

        # proceed the target
        while occupied_seats and occupied_seats[0][0] <= t_arrival:
            _, released_seat = heapq.heappop(occupied_seats)
            heapq.heappush(vacant_seats, released_seat)

        return vacant_seats[0] if vacant_seats else last_seat_num

