'''
2025/02/15 daily challenge

backtracking approach
'''


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def dfs(s, i, curr_sum, target):
            if i == len(s):
                return curr_sum == target
            if curr_sum > target:
                return False
            for j in range(i + 1, len(s) + 1):
                next_sum = curr_sum + int(s[i:j])
                if dfs(s, j, next_sum, target):
                    return True
            return False

        ans = 0
        for k in range(1, n + 1):
            sq = k * k
            if dfs(str(sq), 0, 0, k):
                ans += sq

        return ans

