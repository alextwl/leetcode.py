'''
leetcode 75 lv2 day 20

time=O(n!) recursive approach
'''


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        stack = []
        visited = [0] * n  # flags indicating nums were pushed to stack or not.

        def p():
            '''
            add non-visited nums to the permutation
            '''
            if len(stack) == n:
                ans.append(stack.copy())
                return

            for i in range(n):
                if visited[i] == 0:
                    visited[i] = 1
                    stack.append(nums[i])
                    p()  # add next num
                    visited[i] = 0
                    stack.pop()
            return

        p()
        return ans

