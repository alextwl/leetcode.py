'''
leetcode 75 lv2 day 20

recursive approach

subtract candidates from the target recursively.
when target reaches zero, a valid combination is produced.
'''


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        stack = []

        def findSum(target, i):
            '''
            :param target: remaining sum of target
            :param i: the index of a candidate
            '''
            if target == 0:
                ans.append(stack.copy())
                return
            
            while(i < len(candidates) and (next_target := target - candidates[i]) >= 0):
                stack.append(candidates[i])

                # an index may be revisited in multiple times, so we do **not** increase i here.
                # continue searching target sum.
                findSum(next_target, i)

                # to find combinations containing next candidate, the current candidate should be popped from stack.
                i += 1
                stack.pop()
            return

        '''
        sorting candidates
        '''
        candidates.sort()

        '''
        recursively subtract a candidate from the target,
        when target==0 in findSum() invoked, a valid combination in stack is produced.
        '''
        findSum(target, 0)

        return ans

