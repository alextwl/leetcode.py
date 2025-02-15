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


'''
partition size limited ver
'''


class Solution:
    def punishmentNumber(self, n: int) -> int:
        def dfs(num, target):
            if target < 0 or num < target:
                return False
            if num == target:
                return True
            # since there's 1 <= n <= 1000 constraint,
            # we can just limit the size of each partition within 1000.
            for j in [10, 100, 1000]:
                quo, rem = divmod(num, j)
                if dfs(quo, target - rem):
                    return True
            return False

        ans = 0
        for k in range(1, n + 1):
            sq = k * k
            if dfs(sq, k):
                ans += sq

        return ans

