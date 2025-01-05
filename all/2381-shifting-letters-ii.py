'''
2025/01/05 daily challenge

prefix sum approach

the prefixes are the differences of shiftings.
'''


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        prefix = [0] * (len(s) + 1)
        for start, end, sign in shifts:
            if sign:
                prefix[start] += 1
                prefix[end+1] -= 1
            else:
                prefix[start] -= 1
                prefix[end+1] += 1

        ans = []
        curr_diff = 0
        a = ord('a')
        for c, diff in zip(s, prefix):
            curr_diff += diff
            ans.append(chr(((ord(c) - a + curr_diff) % 26) + a))

        return ''.join(ans)

