'''
2026/03/02 daily challenge

simulation approach
'''


class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        # find the rightmost one for each row
        rightmost_one = []
        for row in grid:
            last = -1
            for i, v in enumerate(row):
                if v == 1:
                    last = i
            rightmost_one.append(last)

        # simulate the process
        swaps = 0
        for i in range(n):
            if i < rightmost_one[i]:
                # find the nearest target and swap
                for j in range(i + 1, n):
                    if rightmost_one[j] <= i:
                        v = rightmost_one.pop(j)
                        rightmost_one.insert(i, v)
                        swaps += j - i
                        break
                else:
                    # answer does not exist.
                    return -1
        return swaps

