'''
2025/09/09 daily challenge

simulation + queue (FIFO) approach

learnt from official editorial:
https://leetcode.com/problems/number-of-people-aware-of-a-secret/editorial/#approach-simulation--deque
'''


import collections


class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        q_known = collections.deque()  # (day, count of known ppl)
        q_sharing = collections.deque()  # (day, count of ppl sharing secret)

        cnt_known = 1
        q_known.append((1, 1))  # day 1 one person discovers a secret
        cnt_sharing = 0

        for curr_day in range(2, n + 1):
            if q_known and q_known[0][0] == curr_day - delay:
                # people start sharing secret after delay
                d, ppl = q_known.popleft()
                cnt_known -= ppl
                cnt_sharing += ppl
                q_sharing.append((d, ppl))
            if q_sharing and q_sharing[0][0] == curr_day - forget:
                # people forget secret
                cnt_sharing -= q_sharing.popleft()[1]
            if q_sharing:
                # share secret to more people
                cnt_known += cnt_sharing
                q_known.append((curr_day, cnt_sharing))  # (today, new people)
        return (cnt_known + cnt_sharing) % 1_000_000_007

