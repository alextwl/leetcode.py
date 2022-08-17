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
