'''
monotonic stack approach
'''


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        # monotonic strictly decreasing stack
        stack = []  # (v, i)
        for i, v in enumerate(nums):
            while stack and stack[-1][0] < v:
                ans[stack.pop()[1]] = v
            stack.append((v, i))

        # circular array, traverse it again
        # without pushing new numbers to stack.
        for v in nums:
            if stack:
                while stack and stack[-1][0] < v:
                    ans[stack.pop()[1]] = v
            else:
                break

        return ans

