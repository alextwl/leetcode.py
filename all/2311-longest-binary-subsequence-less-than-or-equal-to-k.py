'''
2025/06/26 daily challenge

greedy method approach

include all 0's bits and try to pick 1's bits from LSB.
'''


class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        stack = list(s)
        sub = 0
        sub_len = 0
        k_len = k.bit_length()  # we pick 1's bits up within k's bit length.
        while stack:
            c = stack.pop()
            if c == '1' and sub_len < k_len and (next_sub := sub + (1 << sub_len)) <= k:
                sub = next_sub
                sub_len += 1
            elif c == '0':
                # 0 is always included since leading zeros were allowed
                sub_len += 1
        return sub_len

