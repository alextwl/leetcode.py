'''
2026/03/28 daily challenge

greedy method approach

learnt from official editorial:
https://leetcode.com/problems/find-the-string-with-lcp/editorial/#approach-greedy-construction
'''


ASCII_Z = ord('z')


class Solution:
    def findTheString(self, lcp: List[List[int]]) -> str:
        n = len(lcp)
        word = [""] * n
        curr = ord('a')

        # construct string from a to z lexicographically.
        for i, lcp_i in enumerate(lcp):
            if not word[i]:
                if curr > ASCII_Z:
                    return ""
                word[i] = curr_chr = chr(curr)
                for j in range(i + 1, n):
                    if lcp_i[j]:
                        word[j] = curr_chr
                curr += 1
        
        # bottom-up check if the generated string meets LCP
        for i in range(n - 1, -1, -1):
            chr_i = word[i]
            for j in range(n - 1, -1, -1):
                if chr_i != word[j]:
                    if lcp[i][j]:
                        # no common prefix, lcp[i][j] should be zero.
                        return ""
                else:
                    if i == n - 1 or j == n - 1:
                        if lcp[i][j] != 1:
                            # both substring starts from terminal,
                            # LCP length is impossible to be greater than 1.
                            return ""
                    else:
                        if lcp[i][j] != lcp[i+1][j+1] + 1:
                            # cannot extend LCP from lcp[i+1][j+1]
                            return ""
        return "".join(word)

