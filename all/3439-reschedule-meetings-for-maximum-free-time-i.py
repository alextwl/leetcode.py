'''
2025/07/09 daily challenge

greedy method + prefix sum approach

learnt from official editorial 1:
https://leetcode.com/problems/reschedule-meetings-for-maximum-free-time-i/editorial/#approach-1-greedy--prefix-sum
'''


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        if eventTime == n:
            return 0

        ans = 0
        prefix = [0]  # prefix[i] = the prefix sum of meeting durations before meeting i
        for i, (t0, t1) in enumerate(zip(startTime, endTime)):
            prefix.append(prefix[i] + t1 - t0)
        
        n1 = n - 1
        k1 = k - 1
        # try to shift k consecutive meetings together and merge free slots nearby.
        for i in range(k - 1, n):
            # determine the start time of 1st avail time slot before k meetings
            if i == k1:
                left = 0
            else:
                left = endTime[i - k]
            # determine the end time of last avail time slot after k meetings
            if i == n1:
                right = eventTime
            else:
                right = startTime[i + 1]
            # total free time in a slot = right end - left start - duration of k meetings in the middle
            ans = max(ans, right - left - (prefix[i + 1] - prefix[i - k + 1]))

        return ans


'''
sliding window approach
'''


class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        if eventTime == n:
            return 0

        ans = 0
        n1 = n - 1
        k1 = k - 1
        t = 0  # duration of meetings in the window
        for i, (t0, t1) in enumerate(zip(startTime, endTime)):
            t += t1 - t0
            if i <= k1:
                left = 0
            else:
                left = endTime[i - k]
            if i == n1:
                right = eventTime
            else:
                right = startTime[i + 1]
            ans = max(ans, right - left - t)
            # remove oldest meeting duration out of window
            if i >= k - 1:
                t -= endTime[i - k + 1] - startTime[i - k + 1]
        return ans

