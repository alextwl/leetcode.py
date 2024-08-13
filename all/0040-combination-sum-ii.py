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

