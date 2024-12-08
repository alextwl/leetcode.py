'''
2024/12/08 daily challenge

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

