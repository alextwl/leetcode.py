'''
2025/11/18 daily challenge

if a bit started as 1, that must be a two-bit character which
consists of either 11 or 10, so try to decode it as the 2nd char,
and then the 1st.
'''


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # shortcut
        if bits[-1] == 0 and len(bits) > 1 and bits[-2] == 0:
            return True

        it = iter(bits)
        ans = False
        for v in it:
            if v:
                # 2nd: two-bit char
                next(it)  # the next bit is irrelevant
                ans = False
            else:
                # 1st: one-bit char
                ans = True
        return ans

