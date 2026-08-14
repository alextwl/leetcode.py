'''
2026/08/14 daily challenge

sliding window approach
'''


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ctr = {chr(ord('a') + i): 0 for i in range(26)}

        j = 0
        exceeded = 0
        for i, c in enumerate(s):
            ctr[c] += 1
            if ctr[c] == 3:
                exceeded += 1

            if exceeded:
                ctr[s[j]] -= 1
                if ctr[s[j]] == 2:
                    exceeded -= 1
                j += 1

        return len(s) - j

