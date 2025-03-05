'''
math approach

for odd slice(s) they need n cuts, for even slices they need n/2 cuts.
for only 1 slice, no need to cut.
'''


class Solution:
    def numberOfCuts(self, n: int) -> int:
        if n == 1:
            return 0
        return n if n & 1 else n >> 1

