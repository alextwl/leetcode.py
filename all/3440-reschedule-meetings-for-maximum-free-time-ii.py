'''
2025/07/10 daily challenge

greedy method + hash approach
'''


import bisect
import collections


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        n1 = n - 1

        # scan all empty slots
        emptys = collections.defaultdict(list)  # emptys[t] = [startTime(s), ...]
        prev = 0  # previous beginning of an empty slot
        for t0, t1 in zip(startTime, endTime):
            if t0 > prev:
                emptys[t0 - prev].append(prev)
            prev = t1
        if prev < eventTime:
            emptys[eventTime - prev].append(prev)

        slot_lens = sorted(emptys.keys())

        # scan meetings and try to reschedule
        ans = 0
        prev = 0
        for i, (t0, t1) in enumerate(zip(startTime, endTime)):
            m_len = t1 - t0
            # the right bound of current possible slot (prior to the next meeting)
            t_right = eventTime if i == n1 else startTime[i+1]
            # try to reschedule the current meeting to other slots,
            # the slot cannot be in the range of endTime[i-1] to startTime[i+1]
            found = 0
            # binary search the duration of free slots equal or larger than the current meeting
            for j in range(bisect.bisect_left(slot_lens, m_len), len(slot_lens)):
                for t_free in emptys[slot_lens[j]]:
                    if t_free < prev or t_free > t_right:
                        ans = max(ans, t_right - prev)
                        found = 1
                        break
                if found:
                    break
            else:
                # no other slot available,
                # shift the current meeting to combine slot of both sides
                ans = max(ans, t_right - prev - m_len)
            prev = t1

        return ans

