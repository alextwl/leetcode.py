'''
2025/11/15 daily challenge

counting approach

learnt from official editorial:
https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/editorial/#approach-enumeration
'''


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        pfx = [-1] * (n + 1)  # pfx[i] = the nearest pos of '0' before s[i]
        for i in range(n):
            if i == 0 or s[i - 1] == '0':
                pfx[i + 1] = i
            else:
                pfx[i + 1] = pfx[i]
        
        ans = 0
        # count valid substrings in s[:i]
        for i, c in enumerate(s, start=1):
            if c == '0':
                # the first iteration of while-loop for s[pfx[j]:i] is
                # s[i-1:i] if last char of s[:i] was zero,
                # so we need to count it in advance.
                zeros = 1
            else:
                zeros = 0

            j = i
            # extend the left bound from s[pfx[j]:i]
            while j > 0 and zeros * zeros <= n:
                # calculate the number of ones in s[pfx[j]:i]
                # (i - pfx[j]) is the length of s[pfx[j]:i]
                ones = (i - pfx[j]) - zeros
                if zeros * zeros <= ones:
                    ans += min(j - pfx[j], ones - zeros * zeros + 1)
                # count next zero in the left
                j = pfx[j]
                zeros += 1

        return ans

