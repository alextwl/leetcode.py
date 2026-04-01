class Solution:
    def maxPower(self, s: str) -> int:
        max_len = curr_len = 0
        prev = None
        for c in s:
            if prev == c:
                curr_len += 1
            else:
                max_len = max(max_len, curr_len)
                prev = c
                curr_len = 1
        return max(max_len, curr_len)

