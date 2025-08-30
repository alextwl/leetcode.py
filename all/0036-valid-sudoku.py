class Solution:
    def isValidSet(self, setlist: List[str]) -> bool:
        seen = {}
        for val in setlist:
            if val == '.':
                continue
            if val in seen:
                return False
            seen[val] = 1
        return True
        
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # examine each row
        for rowlist in board:
            if not self.isValidSet(rowlist):
                return False
        
        # examine each column
        for col in range(0,9):
            collist = []
            for row in range(0,9):
                collist.append(board[row][col])
            if not self.isValidSet(collist):
                return False
        
        # examine each 3x3 sub-box
        for row in range(0,9,3):
            for col in range(0,9,3):
                boxlist = []
                for i in range(0,3):
                    for j in range(0,3):
                        boxlist.append(board[row+i][col+j])
                if not self.isValidSet(boxlist):
                    return False

        # all conditions passed
        return True


'''
2025/08/30 daily challenge
'''


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        xset = [set() for _ in range(9)]
        yset = [set() for _ in range(9)]

        for x0 in range(0, 9, 3):
            for y0 in range(0, 9, 3):
                curr = set()
                for i in range(x0, x0 + 3):
                    for j in range(y0, y0 + 3):
                        v = board[i][j]
                        if v == ".":
                            continue
                        if v in curr or v in xset[i] or v in yset[j]:
                            return False
                        curr.add(v)
                        xset[i].add(v)
                        yset[j].add(v)
        return True

