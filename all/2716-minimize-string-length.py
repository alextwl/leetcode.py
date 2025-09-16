'''
set approach

operations performed until last occurrence of specific char remained.
'''


class Solution:
    def minimizedStringLength(self, s: str) -> int:
        return len(set(s))

