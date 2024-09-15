'''
2024/09/15 daily challenge

bitmask + prefix XOR approach
'''


class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        a = ord('a')
        c2mask = [0] * 26
        for i, c in enumerate("aeiou"):
            c2mask[ord(c) - a] = 1 << i

        # position of first seen prefix bitmask
        # (**not** last seen because we need to get the longest substring.)
        mask_pos = [-1] * 32

        prefix = 0
        longest = 0
        for i, c in enumerate(s):
            prefix ^= c2mask[ord(c) - a]
            if prefix and mask_pos[prefix] == -1:
                mask_pos[prefix] = i

            longest = max(longest, i - mask_pos[prefix])

        return longest

