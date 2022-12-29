'''
leetcode 75 lv1 day 5

counter approach
'''

import collections

class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_amount = collections.Counter(s)

        center_char = 0
        half_length = 0

        for amount in char_amount.values():
            #quo, mod = divmod(amount, 2)
            half_length += amount >> 1
            center_char |= amount & 1  # to decide if we could have a center char

        return half_length*2 + center_char

