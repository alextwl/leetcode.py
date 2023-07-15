'''
2023/07/15 daily challenge

dynamic programming (top-down) + binary search approach

learnt from official solution
https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/solution/
'''

import bisect


class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)

        # sort events by start time (also the 1st element of each event list)
        events.sort()
        # filter only the start time because bisect cannot evaluate list element.
        starts = [s for s, _, _ in events]
        # dp[k_count][event_index] = the maximum value when the event_index evaluated (attended or not attended) with k_count remaining.
        dp = [[-1] * n for _ in range(k+1)]
        
        def dfs(k_count, i_event):
            if k_count == 0:
                # no event attended means the maximum value is always zero.
                return 0
            if i_event == n:
                # no more events can be attended after the last event.
                return 0
            if dp[k_count][i_event] != -1:
                return dp[k_count][i_event]
            
            start_day, end_day, event_value = events[i_event]
            
            '''
            we use bisect_right here because an event starts at start_day and
            ends at end_day, both terminal days are inclusive,
            so we must select the next event not earlier than the day next to the current end_day.
            '''
            next_event = bisect.bisect_right(starts, end_day)
            
            '''
            dp[k_count][i_event] = max(bypass this event and go to the event next to the current event,
                                       attend this event and go to the event started after the current end_day.)
            '''
            max_val = dp[k_count][i_event] = max(dfs(k_count, i_event + 1),
                                                 event_value + dfs(k_count - 1, next_event))
            
            return max_val

        return dfs(k, 0)

