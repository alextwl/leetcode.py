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


'''
2023/09/08 daily challenge
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        last_row = [1]
        pascals = [last_row]
        
        for _ in range(1, numRows):
            new_row = [1]
            it = iter(last_row)
            prev = next(it)
            for curr in it:
                new_row.append(prev + curr)
                prev = curr
            new_row.append(1)
            pascals.append(new_row)
            last_row = new_row

        return pascals

