'''
2023/01/24 daily challenge
2025/05/31 daily challenge

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


'''
level order traversal approach
'''


import collections


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # flatten the board (serialize into 1D array)
        n = len(board)
        n2 = n * n
        arr = [0]
        rev = 0
        for row in reversed(board):
            if rev:
                arr += row[::-1]
            else:
                arr += row
            rev ^= 1

        # BFS
        q = collections.deque([1])
        visited = set()
        dice_rolls = 1
        while q:
            width = len(q)
            for _ in range(width):
                node = q.popleft()
                if node in visited:
                    continue
                visited.add(node)
                for next_hop in range(node + 1, min(node + 6, n2) + 1):
                    if arr[next_hop] != -1:
                        next_hop = arr[next_hop]
                    if next_hop == n2:
                        return dice_rolls
                    q.append(next_hop)
            dice_rolls += 1
        return -1

