'''
2024/12/08 daily challenge
2025/12/23 daily challenge

dynamic programming + binary search approach (top-down)

run DP with k events picked at the events[i],
and binary search **next** event non-overlapped with events[i].
'''


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        # dp[i][k] = k events picked at the events[i]
        dp = [[-1] * 3 for _ in range(n)]

        events.sort()  # order by start time

        def pickup(i, k):
            # max 2 events
            if k == 2 or i >= n:
                return 0

            if dp[i][k] == -1:
                _, endtime, value = events[i]

                # binary search **next** event non-overlapped with events[i]
                left, right = i + 1, n - 1
                while left < right:
                    mid = (left + right) // 2
                    if events[mid][0] > endtime:
                        right = mid
                    else:
                        left = mid + 1

                # pick events[i] and iterate next non-overlapped event
                if left < n and events[left][0] > endtime:
                    max_sum = value + pickup(left, k + 1)
                else:
                    max_sum = value

                # **NOT** to pick events[i] up and iterate the event next to i
                max_sum = max(max_sum, pickup(i + 1, k))
                dp[i][k] = max_sum
            return dp[i][k]

        return pickup(0, 0)


'''
min heap approach

(1) push events to min-heap
(2) pop previous non-overlapped events and try to maximize the previous maximum value
(3) try to pair the max value with the current event's value
'''


import heapq


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()

        h = []

        max_value = 0  # maximum value of an event we've seen. (and it might be paired with current event)
        max_sum = 0

        for starttime, endtime, value in events:
            # pop all previous non-overlapped events and consider if we can pick its value.
            while h and h[0][0] < starttime:
                _, v = heapq.heappop(h)
                max_value = max(max_value, v)

            # try to pair the previous maximum value with the current event's value.
            max_sum = max(max_sum, max_value + value)

            # push to min heap to be a candidate for further possible pairs.
            heapq.heappush(h, (endtime, value))

        return max_sum


'''
greedy method approach (line sweep algorithm)

learnt from official solution 3:
https://leetcode.com/problems/two-best-non-overlapping-events/solution/
'''


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        tv = []  # (time, flag=1 if it's starttime else 0, value)

        # line sweep: reduce a 2D problem (an event with start/end timestamps)
        # into simpler 1D problem. (one timestamp for an element in the array)
        for starttime, endtime, value in events:
            tv.append((starttime, 1, value))
            # increase endtime by 1 to ensure it's sorted after all events overlapped by starttime.
            tv.append((endtime + 1, 0, value))

        tv.sort()  # order by time

        max_value = 0
        max_sum = 0
        for _, flag, v in tv:
            if flag:
                # encounter a start time, try to pair it with previous maximum value.
                #
                # note the value stored in max_value is guaranteed non-overlapped with current event
                # because the endtimes of all overlapped previous events are not yet processed.
                max_sum = max(max_sum, v + max_value)
            else:
                # an event ended, try to maximize the value
                max_value = max(max_value, v)

        return max_sum

