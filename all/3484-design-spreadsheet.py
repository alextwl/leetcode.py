'''
2025/09/19 daily challenge
'''


col2j = {c: j for j, c in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ")}


class Spreadsheet:
    def __init__(self, rows: int):
        self.rows = rows
        self.sheet = [[0] * 26 for _ in range(rows + 1)]

    def setCell(self, cell: str, value: int) -> None:
        j, i = col2j[cell[0]], int(cell[1:])
        self.sheet[i][j] = value

    def resetCell(self, cell: str) -> None:
        self.setCell(cell, 0)

    def getValue(self, formula: str) -> int:
        operands = formula[1:].split('+')
        ret = 0
        for s in operands:
            if s[0].isalpha():
                j, i = col2j[s[0]], int(s[1:])
                ret += self.sheet[i][j]
            else:
                ret += int(s)
        return ret

