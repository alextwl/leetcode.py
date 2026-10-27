'''
2026/10/27 daily challenge

move to the rightmost and then go down until the end
'''


class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        grid = ['.' * n]
        row = '#' * (n - 1) + '.'
        for _ in range(1, m):
            grid.append(row)
        return grid

