'''
2026/07/05 daily challenge

bottom-up dynamic programming approach
'''


ASCII_0 = ord('0')


class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        n = len(board)
        # dp[x][y] = [max_score, path_count]
        dp = [[[-1, 0] for _ in range(n)] for _ in range(n)]
        dp[-1][-1] = [0, 1]

        def move(x0, y0, x1, y1):
            # move from previous node (x1, y1) to current node (x0, y0)
            if x1 >= n or y1 >= n:
                # out of bound
                return
            if dp[x1][y1][0] > dp[x0][y0][0]:
                dp[x0][y0] = dp[x1][y1].copy()
            elif dp[x1][y1][0] == dp[x0][y0][0]:
                # add path count for the same max score
                dp[x0][y0][1] += dp[x1][y1][1]

        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if board[i][j] not in "XS":
                    # move from previous nodes to (i, j)
                    move(i, j, i + 1, j)
                    move(i, j, i, j + 1)
                    move(i, j, i + 1, j + 1)
                    if dp[i][j][0] >= 0 and board[i][j] != "E":
                        dp[i][j][0] += ord(board[i][j]) - ASCII_0
        
        if dp[0][0][0] == -1:
            # no valid path
            return [0, 0]
        return [dp[0][0][0], dp[0][0][1] % 1_000_000_007]

