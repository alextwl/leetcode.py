'''
2024/02/18 daily challenge

min heap approach

use min heaps to store empty rooms,
and (end time, room) of meetings being held.
'''

import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        counts = [0] * n  # the number of each room held the meetings
        empty_rooms = list(range(n))  # min heap containing empty room numbers
        occupied = []  # min heap: (end time, room number)

        for i_start, i_end in sorted(meetings):
            # clearing all rooms where its meeting ended
            while(occupied and occupied[0][0] <= i_start):
                _, room = heapq.heappop(occupied)
                heapq.heappush(empty_rooms, room)
            
            if empty_rooms:
                # allocate an empty room
                room = heapq.heappop(empty_rooms)
            else:
                # no rooms available, delay the meeting
                # and allocate the room where a meeting held ends earliest.
                j_end, room = heapq.heappop(occupied)
                i_end = j_end + (i_end - i_start)  # delay the end time

            counts[room] += 1
            heapq.heappush(occupied, (i_end, room))

        # return the lowest room number with maximum number of held meetings
        max_count = 0
        ans = -1
        for i, cnt in enumerate(counts):
            if cnt > max_count:
                max_count = cnt
                ans = i

        return ans

