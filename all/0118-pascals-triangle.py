class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows = [[1]]
        
        for rowIdx in range(1, numRows):
            row = [0] * (rowIdx+1)
            row[0] = 1
            row[-1] = 1
            for col in range(1, rowIdx):
                row[col] = rows[-1][col-1] + rows[-1][col]
            rows.append(row)
        
        return rows
