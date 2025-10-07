'''
2025/10/07 daily challenge

binary search approach
'''


import bisect


class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        fulls = dict()
        drys = []  # dry days available
        ans = []

        for i, v in enumerate(rains):
            if v == 0:
                ans.append(1)  # lake index starts from 1.
                drys.append(i)
            else:
                ans.append(-1)
                if v in fulls:
                    if not drys or drys[-1] < fulls[v]:
                        return []
                    # binary search the nearest non-rain day
                    # after last day the lake is full to dry the lake.
                    j = bisect.bisect_left(drys, fulls[v])
                    ans[drys.pop(j)] = v

                fulls[v] = i

        return ans

