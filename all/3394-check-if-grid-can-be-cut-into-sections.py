'''
2025/03/25 daily challenge

interval merger approach
'''


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def can_cut(intervals):
            intervals.sort()
            sections = 0
            prev_end = -1
            for a, b in intervals:
                if a >= prev_end:
                    sections += 1
                    if sections == 3:
                        # shortcut: the question asks for only 3 resulting sections
                        return True
                if prev_end < b:
                    prev_end = b
            return sections >= 3

        row_intvals = []
        col_intvals = []
        for x0, y0, x1, y1 in rectangles:
            row_intvals.append((x0, x1))
            col_intvals.append((y0, y1))

        return can_cut(row_intvals) or can_cut(col_intvals)

