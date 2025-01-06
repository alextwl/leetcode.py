'''
2025/01/06 daily challenge

prefix sum approach

build prefix & suffix sums of balls and accumulate moves in both directions.
'''


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # prefix
        curr_balls = 0
        move_sum = 0
        ans = []

        for c in boxes:
            move_sum += curr_balls
            ans.append(move_sum)
            if c == '1':
                curr_balls += 1

        # suffix
        curr_balls = 0
        move_sum = 0
        for i, c in enumerate(reversed(boxes), start=1):
            move_sum += curr_balls
            ans[-i] += move_sum
            if c == '1':
                curr_balls += 1

        return ans

