'''
2025/10/09 daily challenge

O(mn) brute-force approach

learnt from hints.
'''


class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        n = len(skill)
        f = [0] * n  # earlist available time for each wizard
        for x in mana:
            now = f[0]
            for i in range(1, n):
                now = max(now + skill[i - 1] * x, f[i])
            f[-1] = now + skill[-1] * x
            for i in range(n - 2, -1, -1):
                f[i] = f[i + 1] - skill[i + 1] * x
        return f[-1]

