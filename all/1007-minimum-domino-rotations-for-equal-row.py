'''
2025/05/03 daily challenge

two-pass set approach
'''


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        n = len(tops)
        # find equal elements
        equals = {tops[0], bottoms[0]}
        for a, b in zip(tops, bottoms):
            if a == b:
                # so it's an equal column
                n -= 1  # deduct count of equal column
                if a not in equals:
                    # shortcut: if it's not existed in previous dominos,
                    # we cannot make an equal row in either tops or bottoms.
                    return -1
                # we have only one equal element so far.
                equals = {a}
            else:
                # try to do AND operation with previous equal elements.
                curr = {a, b}
                equals &= curr
            if not equals:
                # shortcut: the equal element is not existed
                return -1

        # find minimum swaps
        ans = float('inf')
        for eq in equals:
            eq_in_tops = 0
            for a, b in zip(tops, bottoms):
                if a != b and a == eq:
                    eq_in_tops += 1
            ans = min(ans, eq_in_tops, n - eq_in_tops)

        return ans

