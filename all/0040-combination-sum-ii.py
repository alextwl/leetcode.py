'''
2024/08/13 daily challenge

backtracking approach
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        n = len(candidates)
        candidates.sort()

        def backtrack(target, pos, path):
            if target < 0:
                # negative sum, cannot form a valid combination
                return
            if target == 0:
                # hit target sum, can form a valid combination
                ans.append(path)
                return

            prev = None
            for i in range(pos, n):
                # check if candidates[i] was a duplicate of the previous element,
                # no need to invoke duplicate backtracing calls.
                if prev == candidates[i]:
                    continue
                prev = candidates[i]
                backtrack(target - prev, i + 1, path + [prev])
            return

        backtrack(target, 0, list())
        return ans


'''
dynamic programming approach (bottom-up, iterative)

use set[tuple] to avoid duplicate combinations.
'''


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # filter elements <= target
        nums = [v for v in candidates if v <= target]
        nums.sort()

        # dp[i] = set of unique combination tuples which sum == i
        dp = [set() for _ in range(target + 1)]
        dp[0].add(tuple())

        for i, v in enumerate(nums):
            for j in range(target - v, -1, -1):
                for comb in dp[j]:
                    # select nums[i]
                    new_comb = list(comb) + [v]
                    dp[j+v].add(tuple(new_comb))

        return list(dp[-1])

