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


'''
min heap approach

slower than stack ver.
'''


import heapq


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [-1] * n

        h = []  # min heap: (v, i)
        for i, v in enumerate(nums):
            while h and h[0][0] < v:
                ans[heapq.heappop(h)[1]] = v
            heapq.heappush(h, (v, i))

        # circular array, traverse it again
        # without pushing new numbers to heap.
        for v in nums:
            if h:
                while h and h[0][0] < v:
                    ans[heapq.heappop(h)[1]] = v
            else:
                break

        return ans

