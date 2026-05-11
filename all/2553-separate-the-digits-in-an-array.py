'''
2026/05/11 daily challenge

arithmetic + stack approach
'''


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans = []
        stack = []
        for v in nums:
            while v >= 10:
                v, rem = divmod(v, 10)
                stack.append(rem)
            ans.append(v)
            while stack:
                ans.append(stack.pop())
        return ans

