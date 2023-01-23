'''
leetcode 75 lv2 day 17

sort + stack approach
'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()  # sort it first.
        stack = []  # new intervals

        for intval in intervals:
            if not stack:
                stack.append(intval)
            else:
                prev = stack.pop()
                if min(prev[1], intval[1]) - max(prev[0], intval[0]) >= 0:
                    stack.append([min(prev[0], intval[0]), max(prev[1], intval[1])])
                else:
                    stack.append(prev)
                    stack.append(intval)

        return stack

