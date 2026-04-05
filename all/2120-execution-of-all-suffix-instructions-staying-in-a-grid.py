'''
simulation approach
'''


DIR = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}


class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        m = len(s)
        ans = []
        for i in range(m):
            x, y = startPos
            moves = 0
            for j in range(i, m):
                dx, dy = DIR[s[j]]
                x += dx
                y += dy
                if not(0 <= x < n and 0 <= y < n):
                    # out of grid
                    break
                moves += 1
            ans.append(moves)
        return ans

