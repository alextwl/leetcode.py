'''
2025/02/07 daily challenge

hashmap (using 2 dicts) approach

because the input is large, remove unused colors during iteration
or we will exceed the memory limit.

do not preallocate arrays.
'''


import collections


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball_color = collections.defaultdict(int)
        color_count = collections.defaultdict(int)

        ans = []
        for ball, color in queries:
            orig_color = ball_color[ball]
            if orig_color:
                color_count[orig_color] -= 1
                if color_count[orig_color] == 0:
                    del color_count[orig_color]

            ball_color[ball] = color
            color_count[color] += 1
            ans.append(len(color_count))

        return ans

