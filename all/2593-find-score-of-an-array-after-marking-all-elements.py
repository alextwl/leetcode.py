'''
2024/12/13 daily challenge

min heap approach
'''


import heapq


class Solution:
    def findScore(self, nums: List[int]) -> int:
        mark = [False] * len(nums)
        h = []
        for i, v in enumerate(nums):
            heapq.heappush(h, (v, i))

        end = len(nums) - 1
        score = 0
        while h:
            v, i = heapq.heappop(h)
            if mark[i]:
                continue
            score += v
            if i > 0:
                mark[i-1] = True
            mark[i] = True
            if i < end:
                mark[i+1] = True
        return score


'''
monotonic stack approach

time=O(n)
'''


class Solution:
    def findScore(self, nums: List[int]) -> int:
        stack = []  # a decreasing stack
        score = 0

        for v in nums:
            if not stack or v < stack[-1]:
                stack.append(v)
            else:
                while stack:
                    score += stack.pop()
                    if stack:
                        # skip neighbor because it's marked
                        stack.pop()
        while stack:
            score += stack.pop()
            if stack:
                stack.pop()

        return score

