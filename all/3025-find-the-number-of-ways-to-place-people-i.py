'''
2025/09/02 daily challenge

brute force approach
'''


class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        n = len(points)
        ans = 0

        for i, (x0, y0) in enumerate(points):
            for j, (x1, y1) in enumerate(points):
                if i == j or not (x0 <= x1 and y0 >= y1):
                    # skip the same coord and
                    # pairs which didn't satisfy the condition of
                    # "A is on the upper left side of B."
                    continue
                
                # check if any coordinate resides in the rectangle formed by i & j.
                for k, (x2, y2) in enumerate(points):
                    if k == i or k == j:
                        continue
                    if (x0 <= x2 <= x1) and (y1 <= y2 <= y0):
                        break
                else:
                    # no violations found, good to count a pair.
                    ans += 1
        return ans

