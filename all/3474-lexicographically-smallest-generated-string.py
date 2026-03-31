'''
2026/03/31 daily challenge

greedy method approach

learnt from official editorial:
https://leetcode.com/problems/lexicographically-smallest-generated-string/editorial/#approach-greedy

(1) initialize word as all-'a' string.
    (which is lexicographical smallest of length n + m - 1)
(2) assign str2 to all 'T'-substrings in word.
(3) make str2 and 'F'-substrings in word different.
'''


class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n, m = len(str1), len(str2)
        nm1 = n + m - 1
        s = ['a'] * nm1
        fixed = [False] * nm1

        # process 'T' and make characters fixed.
        for i, c1 in enumerate(str1):
            if c1 == 'T':
                for j, c2 in enumerate(str2, start=i):
                    if fixed[j] and s[j] != c2:
                        # violation found, cannot make s[i:i+m] == str2
                        # because s[j] is fixed but differ from str2[j-i].
                        return ""
                    s[j] = c2
                    fixed[j] = True
        
        # process 'F'
        for i, c1 in enumerate(str1):
            if c1 == 'F':
                # check if there's at least one different char
                # between str2 and s[i:i+m]
                if any(str2[j - i] != s[j] for j in range(i, i + m)):
                    continue
                
                # find a modification position from the end of substring
                # because we need to make s lexicographically smallest
                for j in range(i + m - 1, i - 1, -1):
                    if not fixed[j]:
                        s[j] = 'b'
                        break
                else:
                    # cannot find a position
                    return ""
        return "".join(s)

