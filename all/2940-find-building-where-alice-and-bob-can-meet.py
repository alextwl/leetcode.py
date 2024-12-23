'''
2024/12/22 daily challenge

monotonic stack + binary search approach

learnt from official solution:
https://leetcode.com/problems/find-building-where-alice-and-bob-can-meet/solution/
'''


class Solution:
    def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:
        ans = [-1] * len(queries)

        new_q = [list() for _ in range(len(heights))]

        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a

            if heights[b] > heights[a] or a == b:
                # in a < b case, if b's height was higher than a's,
                # then a & b will definitely meet at b.
                ans[i] = b
            else:
                new_q[b].append((heights[a], i))

        # monotonic stack: strictly decreasing
        # store "next taller building's height."
        # note stack[0] is the farthest and stack[-1] is the nearest
        # from the current query (building of y.)
        stack = []
        for i in range(len(heights) - 1, -1, -1):
            width = len(stack)
            for h, j in new_q[i]:
                # binary search
                left, right = 0, width - 1
                pos = -1
                # (left) farthest&higher...nearest&lower (right)
                while left <= right:
                    mid = (left + right) // 2
                    if stack[mid][0] > h:
                        pos = max(pos, mid)
                        left = mid + 1
                    else:
                        right = mid - 1
                if pos < width and pos >= 0:
                    ans[j] = stack[pos][1]
            while stack and stack[-1][0] <= heights[i]:
                stack.pop()
            stack.append((heights[i], i))

        return ans
