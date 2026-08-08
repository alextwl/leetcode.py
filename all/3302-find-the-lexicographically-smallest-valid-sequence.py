'''
2026/08/08 daily challenge

prefix & suffix decomposition + greedy method approach

learnt from official editorial:
https://leetcode.com/problems/find-the-lexicographically-smallest-valid-sequence/editorial/#approach-prefix-and-suffix-decomposition--greedy
'''


class Solution:
    def validSequence(self, word1: str, word2: str) -> List[int]:
        n, m = len(word1), len(word2)
        # last[i] = rightmost index in word1 matched word2[i..m-1]
        last = [-1] * m
        j = m - 1
        # traverse both word1 & word2 reversely
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1

        ans = []
        j = 0
        change_quota = 1  # we can change at most 1 char in word1
        for i, c in enumerate(word1):
            if j == m:
                # all m chars matched, no need to traverse for larger order
                break

            if c == word2[j]:
                # match word2[j] greedily for lexicographically smallest
                ans.append(i)
                j += 1
            elif change_quota and (j == m - 1 or i < last[j + 1]):
                # try to change the current char if quota's still avail
                # and current position is before last position of word2[j + 1]
                change_quota -= 1
                ans.append(i)
                j += 1

        if j != m:
            # cannot match all chars
            return []

        return ans

