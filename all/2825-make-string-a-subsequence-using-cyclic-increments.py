'''
2024/12/04 daily challenge

depth first search approach (TLE)
'''


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        m, n = len(str1), len(str2)

        def dfs(i, j):
            if j == n:
                # fully matched str2, we can make a valid subseq
                return True
            if i == m:
                # reached str1 end, insufficient char to make a subseq
                return False

            if str1[i] == 'z':
                c2 = 'a'
            else:
                c2 = chr(ord(str1[i]) + 1)

            # NOT add str1[m] or cyclic next char to the set
            r1 = dfs(i+1, j)

            # try to add str1[m] or cyclic next char to the set
            if str2[j] == str1[i] or str2[j] == c2:
                r2 = dfs(i+1, j+1)
            else:
                r2 = False

            return r1 or r2

        return dfs(0, 0)


'''
one-pass greedy method + two pointer approach
'''


class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        n = len(str2)

        j = 0
        for i, c1 in enumerate(str1):
            c2 = 'a' if c1 == 'z' else chr(ord(c1) + 1)
            if j < n and (c1 == str2[j] or c2 == str2[j]):
                j += 1

        return j == n

