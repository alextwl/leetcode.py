class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start_pos = mlen = 0
        usedChar = dict()
        
        for pos, c in enumerate(s):
            if c in usedChar and start_pos <= usedChar[c]:
                # last repeated char found, reset start pos to the pos next to char's previous pos.
                start_pos = usedChar[c] + 1
            else:
                # non-repeat, increment length
                mlen = max(mlen, pos - start_pos + 1)
            # record last pos of c
            usedChar[c] = pos
        return mlen
