'''
2026/01/13 daily challenge

scanning line (line sweeping + linear algebra) approach

learnt from official editorial 2:
https://leetcode.com/problems/separate-squares-i/editorial/#approach-2-scanning-line
'''


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        total_area = 0
        diffs = []

        for _, y, width in squares:
            # x-coordinate is irrelevant
            total_area += width * width
            diffs.append((y, width, 1))  # bottom bound
            diffs.append((y + width, width, -1))  # top bound

        diffs.sort(key=lambda x: x[0])
        half_total_area = total_area / 2

        covered_width = 0.0
        curr_area = 0.0
        prev_height = 0.0  # y'

        for y, width, delta in diffs:
            dy = y - prev_height
            area = covered_width * dy
            if (curr_area + area) >= half_total_area:
                return prev_height + (total_area - 2 * curr_area) / (2 * covered_width)
            # update covered width
            covered_width += width * delta
            curr_area += area
            prev_height = y

        return 0.0  # undefined behavior

