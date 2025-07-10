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


'''
optimized greedy method approach

learnt from official editorial 2:
https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-ii/editorial/#approach-2-greedy--optimization

scan meetings from both side and track max free slot prior to the current meeting.

time=O(n), space=O(1)
'''


class Solution:
    def maxFreeTime(self, eventTime: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        n1 = n - 1

        ans = 0
        t1 = 0  # the max duration of previous free slots
        t_left = 0  # left bound of free slot prior to the current meeting

        t2 = 0  # the max duration of previous free slots (for reverse scans)
        t_right2 = eventTime  # right bound of free slot next to the current meeting (for reverse scans)
        for i, (m_left, m_right) in enumerate(zip(startTime, endTime)):
            t_right = eventTime if i == n1 else startTime[i + 1]
            duration = m_right - m_left
            if duration <= t1:
                ans = max(ans, t_right - t_left)
            else:
                ans = max(ans, t_right - t_left - duration)
            t1 = max(t1, m_left - t_left)
            t_left = m_right

            # scan reversely by reverse indices only
            t_left2 = 0 if i == n1 else endTime[n - i - 2]
            duration = endTime[n - i - 1] - startTime[n - i - 1]
            if duration <= t2:
                ans = max(ans, t_right2 - t_left2)
            t2 = max(t2, t_right2 - endTime[n - i - 1])
            t_right2 = startTime[n - i - 1]

        return ans

