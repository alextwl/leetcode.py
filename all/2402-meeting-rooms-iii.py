'''
2024/02/18 daily challenge
2025/07/11 daily challenge
2025/12/27 daily challenge

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
        # oneliner:
        # return cnt.index(max(cnt))
        return ans


'''
linear search ver

much slower than min heap
'''


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        room_time = [0] * n  # room[i] = end time of last meeting for room i
        rate = [0] * n

        meetings.sort()
        for t0, t1 in meetings:
            earlist_avail = float('inf')
            target_room = 0
            # linear search available room
            for j in range(n):
                curr_room_end = room_time[j]
                if curr_room_end <= t0:
                    target_room = j
                    break
                if curr_room_end < earlist_avail:
                    earlist_avail = curr_room_end
                    target_room = j
            if room_time[target_room] > t0:
                t1 = room_time[target_room] + (t1 - t0)
            room_time[target_room] = t1
            rate[target_room] += 1

        max_rate = -1
        max_room_id = -1
        for i, cnt in enumerate(rate):
            if cnt > max_rate:
                max_rate = cnt
                max_room_id = i

        return max_room_id

