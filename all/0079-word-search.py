'''
2022/11/24 daily challenge
2024/04/03 daily challenge

depth first search approach

return early to speed up for many exclusion of inputs that's impossible to
find the word without running DFS.
'''

import collections


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        # reject impossible word length
        if len(word) > m * n:
            return False

        # reject insufficient characters needed for input word
        count = collections.Counter(''.join(''.join(row) for row in board))
        for c, freq in collections.Counter(word).items():
            if count[c] < freq:
                return False

        # reverse the word to speed up
        # if the frequency of the first char of the word
        # is larger than the last one in board.
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

        seen = set()

        def dfs(pos, x, y):
            if (x, y) in seen:
                # already searched
                return False

            if board[x][y] != word[pos]:
                # char mismatch
                return False

            seen.add((x, y))

            pos += 1
            if len(word) == pos:
                return True

            for dx, dy in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
                if (0 <= dx < m) and (0 <= dy < n) and dfs(pos, dx, dy):
                    return True

            seen.remove((x, y))

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(0, i, j):
                    return True

        return False

