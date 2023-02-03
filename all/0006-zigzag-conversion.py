'''
2023/02/03 daily challenge
'''


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # corner case:
        if numRows == 1:
            return s

        rows = [""] * numRows  # init char stack for each row

        n = numRows - 1
        r = 0
        topDown = True  # bottomUp if topDown==False
        for c in s:
            rows[r] += c
            # simulate zigzag when reaching top or bottom
            if topDown:
                if r == n:
                    topDown = False
                    r -= 1
                else:
                    r += 1
            else:
                if r == 0:
                    topDown = True
                    r += 1
                else:
                    r -= 1

        return ''.join(rows)

