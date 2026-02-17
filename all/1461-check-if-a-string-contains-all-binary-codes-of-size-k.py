'''
set approach

find the count of distinct binary codes in s.
'''


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        # we need exactly 2**k codes for k-length binary codes
        code_count = 2 ** k
        seen = set()
        for i in range(0, len(s) - k + 1):
            seen.add(s[i:i+k])
            if len(seen) == code_count:
                return True
        return False

