'''
monotonic stack approach
'''


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        v2i = {v: i for i, v in enumerate(nums1)}
        ans = [-1] * len(nums1)
        # monotonic strictly increasing stack
        stack = []  # (v, i)

        for v in nums2:
            while stack and stack[-1][0] < v:
                ans[stack.pop()[1]] = v
            if v in v2i:
                stack.append((v, v2i[v]))

        return ans

