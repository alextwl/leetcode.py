'''
2024/10/21 daily challenge

depth first search approach (backtracking)
'''


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        seen = set()

        def dfs(idx):
            if idx == n:
                return 0

            max_split = 0

            for j in range(idx + 1, n + 1):
                # try each substring starting from s[idx]
                sub = s[idx:j]
                if sub not in seen:
                    seen.add(sub)
                    max_split = max(max_split, dfs(j) + 1)
                    seen.remove(sub)
            return max_split

        return dfs(0)

