'''
2024/06/03 daily challenge

greedy method approach
'''


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        n = len(t)
        j = 0
        tc = t[0]

        for sc in s:
            if sc == tc:
                j += 1
                if j >= n:
                    break
                tc = t[j]

        return n - j

