'''
counter approach
'''


import collections


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        cnt = collections.defaultdict(int)
        cnt[0] = 0

        # count edges in the middle of each row of the wall
        for row in wall:
            right = 0
            for width in row[:-1]:
                right += width
                cnt[right] += 1

        return len(wall) - max(cnt.values())

