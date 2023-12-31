'''
2023/12/31 daily challenge

two pointers approach
'''


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = set()
        max_len = -1

        for i, c in enumerate(s):
            if c in seen:
                continue

            j = s.rfind(c, i+1)
            if j:
                max_len = max(max_len, j - i - 1)
            
            seen.add(c)

        return max_len

