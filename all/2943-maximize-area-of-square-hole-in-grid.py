'''
2026/01/15 daily challenge

sorting approach

sort all bars to be removed, find the largest gaps for
both vertical and horizontal, and find max area for a square.
'''


class Solution:
    def maximizeSquareHoleArea(self, n: int, m: int, hBars: List[int], vBars: List[int]) -> int:
        def get_max_gap(bars):
            curr_len = max_len = 1
            prev = 1
            for v in sorted(bars):
                if prev + 1 == v:
                    curr_len += 1
                else:
                    max_len = max(max_len, curr_len)
                    # removing an bar when its previous bar was kept
                    # creates at least 2 units of gap.
                    curr_len = 2
                prev = v
            return max(max_len, curr_len)

        # so we have a largest rectangle here.
        # shrink it to a square.
        max_width = min(get_max_gap(hBars), get_max_gap(vBars))
        return max_width * max_width

