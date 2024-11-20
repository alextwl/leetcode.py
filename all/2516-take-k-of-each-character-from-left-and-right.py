'''
2024/11/20 daily challenge

sliding window approach
'''


import collections


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = collections.Counter(s)

        # check if it's possible to get an ans
        for c in "abc":
            if cnt[c] < k:
                return -1

        window_cnt = {c: 0 for c in "abc"}
        max_len = 0  # max window length

        left = 0
        for right, c in enumerate(s):
            window_cnt[c] += 1

            # shrink the window from left
            # no need to shrink more because we want to maximize the window
            if any(cnt[d] - window_cnt[d] < k for d in "abc"):
                window_cnt[s[left]] -= 1
                left += 1

            max_len = max(max_len, right - left + 1)

        return len(s) - max_len

