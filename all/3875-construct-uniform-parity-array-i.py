'''
2026/09/02 daily challenge

math approach

we can always obtain an uniform parity array no matter what nums1 has.

odd - another odd = an even
even - another odd = an odd

if there's no other odd, then we already have an uniform parity array.
'''


class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        return True

