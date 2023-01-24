'''
2023/01/24 daily challenge

breadth first search approach
'''

import collections


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        n2 = n*n

        # scan board and build jumpFrom[src] = dst mapping.
        jumpFrom = dict()
        label = 1
        revRow = False
        for i in range(n-1, -1, -1):
            if revRow:
                r = range(n-1, -1, -1)
            else:
                r = range(n)
            for j in r:
                if board[i][j] > 0:
                    jumpFrom[label] = board[i][j]
                label += 1
            # reverse the traversing direction of next row.
            revRow = not(revRow)
        
        # BFS
        minMoves = dict()  # minimum moves to the key=label.
        q = collections.deque([(1, 0)])  # (label, minimum moves to the label)
        while(q):
            curr, moves = q.popleft()
            if curr in minMoves and minMoves[curr] <= moves:
                # the label was already visited by fewer moves.
                continue
            #print("update minMoves[%d]=%d" % (curr, moves))
            minMoves[curr] = moves
            moves += 1
            if curr < n2:
                # roll the dice
                for label in range(curr+1, min(curr+6, n2)+1):
                    # queue the next stop with checking the board settings (mapped in jumpFrom)
                    q.append((jumpFrom.get(label, label), moves))

        return minMoves.get(n2, -1)

