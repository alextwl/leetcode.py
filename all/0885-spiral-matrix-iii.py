'''
2024/08/08 daily challenge

simulation approach
'''


class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, rStart: int, cStart: int) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        ans = []
        total_cells = rows * cols
        width = 1  # current spiral matrix width
        curr_dir = 0

        x, y = rStart, cStart
        while len(ans) < total_cells:
            for _ in range(2):
                dx, dy = dirs[curr_dir]
                for _ in range(width):
                    # check boundary to determine if it's a valid cell
                    if 0 <= x < rows and 0 <= y < cols:
                        ans.append([x, y])
                    # go forward
                    x, y = x+dx, y+dy
                # turn to the next direction
                curr_dir = (curr_dir + 1) % 4
            # observe the example of spiral matrix,
            # the matrix's width always increases when
            # we've made each 2 turns towarding a new direction.
            width += 1

        return ans

