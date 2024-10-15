'''
2024/10/15 daily challenge

two pointer approach

learnt from official solution:
https://leetcode.com/problems/separate-black-and-white-balls/solution/
'''


class Solution:
    def minimumSteps(self, s: str) -> int:
        white_pos = 0  # the left bound ([:white_pos]) of grouped white ball
        swaps = 0
        
        for i, c in enumerate(s):
            if c == '0':
                # swap the white ball to the left.
                # the difference between i & white_pos is the number of black balls
                # where its positions white ball need to swap with.
                swaps += i - white_pos
                white_pos += 1
        
        return swaps


'''
counter approach

count and accumulate all black balls prior to a white ball.
'''


class Solution:
    def minimumSteps(self, s: str) -> int:
        blacks = 0
        swaps = 0

        for c in s:
            if c == '0':
                swaps += blacks
            else:
                blacks += 1

        return swaps

