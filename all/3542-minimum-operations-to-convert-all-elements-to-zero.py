'''
2025/11/10 daily challenge

monotonic stack approach
'''


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = 0
        stack = []  # strictly increasing
        for v in nums:
            if v == 0:
                if stack:
                    # summarize
                    ans += len(stack)
                    stack = []
            elif not stack:
                stack.append(v)
            else:
                while stack and stack[-1] > v:
                    # count operations for larger numbers
                    stack.pop()
                    ans += 1
                if not stack or stack[-1] != v:
                    stack.append(v)
        ans += len(stack)
        return ans

