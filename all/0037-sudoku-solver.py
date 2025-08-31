'''
2025/08/31 daily challenge

set + backtracking approach
'''


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        allset = set(map(str, range(1, 10)))
        xset = [set() for _ in range(9)]
        yset = [set() for _ in range(9)]
        cubeset = [set() for _ in range(9)]

        def coord2cube(x, y):
            # convert coordinates to index of affiliated cube
            return 3 * (y // 3) + (x // 3)

        # build sets
        for i, row in enumerate(board):
            for j, v in enumerate(row):
                if v != ".":
                    xset[i].add(v)
                    yset[j].add(v)
                    cubeset[coord2cube(i, j)].add(v)

        completed = False

        def next_dfs(x, y):
            y += 1
            if y == 9:
                x += 1
                y = 0
                if x == 9:
                    nonlocal completed
                    completed = True
                    return
            dfs(x, y)

        def dfs(x, y):
            nonlocal completed
            if board[x][y] == ".":
                # try to fill numbers
                cube_idx = coord2cube(x, y)
                for digit in allset - xset[x] - yset[y] - cubeset[cube_idx]:
                    # fill the digit
                    board[x][y] = str(digit)
                    xset[x].add(digit)
                    yset[y].add(digit)
                    cubeset[cube_idx].add(digit)

                    # go to next coordinate
                    next_dfs(x, y)

                    if not completed:
                        # pop the digit
                        xset[x].remove(digit)
                        yset[y].remove(digit)
                        cubeset[cube_idx].remove(digit)
                    else:
                        break
                else:
                    board[x][y] = "."
            else:
                # already filled, go to next coordinate
                next_dfs(x, y)

        dfs(0, 0)
        return

