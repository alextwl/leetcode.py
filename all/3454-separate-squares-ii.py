'''
2026/01/14 daily challenge

scanning line + segment tree approach

learnt from official editorial:
https://leetcode.com/problems/separate-squares-ii/editorial/#approach-scanning-line--segment-tree

"overlapped areas counted only once" version of problem 3453.
'''


import bisect


class SegmentTree:
    def __init__(self, xlist):
        self.xlist = xlist  # sorted list of distinct x-coordinate intervals
        self.n = len(xlist) - 1
        self.count = [0] * (self.n * 4)
        self.covered = [0] * (self.n * 4)
    
    def update(self, q_left, q_right, q_val, left, right, pos):
        if self.xlist[right + 1] <= q_left or self.xlist[left] >= q_right:
            return

        if q_left <= self.xlist[left] and self.xlist[right + 1] <= q_right:
            self.count[pos] += q_val
        else:
            mid = (left + right) // 2
            self.update(q_left, q_right, q_val, left, mid, pos * 2 + 1)
            self.update(q_left, q_right, q_val, mid + 1, right, pos * 2 + 2)

        if self.count[pos] > 0:
            self.covered[pos] = self.xlist[right + 1] - self.xlist[left]
        else:
            if left == right:
                self.covered[pos] = 0
            else:
                self.covered[pos] = self.covered[pos * 2 + 1] + self.covered[pos * 2 + 2]

    def query(self):
        return self.covered[0]


class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        events = []  # scanning line list: [(y, delta, x_left, x_right)]
        xset = set()  # seen x-coords
        for x_left, y, width in squares:
            x_right = x_left + width
            events.append((y, 1, x_left, x_right))
            events.append((y + width, -1, x_left, x_right))
            xset.add(x_left)
            xset.add(x_right)
        xlist = sorted(xset)

        tree = SegmentTree(xlist)
        events.sort()

        psum = []  # prefix sums of area
        widths = []
        total_area = 0.0
        prev_y = events[0][0]

        for y, delta, x_left, x_right in events:
            length = tree.query()
            total_area += length * (y - prev_y)
            tree.update(x_left, x_right, delta, 0, tree.n - 1, 0)
            psum.append(total_area)
            widths.append(tree.query())
            prev_y = y

        # binary search half of total area as the target in the prefix sum area
        half_area = (total_area + 1) // 2  # round up
        i = bisect.bisect_left(psum, half_area) - 1
        area = psum[i]
        width = widths[i]
        height = events[i][0]

        return height + (total_area - area * 2) / (width * 2.0)

