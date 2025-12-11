'''
2025/12/11 daily challenge

build min/max values vertically (by column) & horizontally (by row)
and count building's coordinates residing in the ranges.
'''


class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        # vertical top & bottom, key=x-coord, value=min/max y-coord
        v_top = [None] * (n + 1)
        v_bottom = [None] * (n + 1)
        # horizontal leftmost & rightmost, key=y-coord, value=min/max x-coord
        h_left = [None] * (n + 1)
        h_right = [None] * (n + 1)

        for x, y in buildings:
            if v_top[x] is None:
                v_top[x] = y
                v_bottom[x] = y
            else:
                if y > v_top[x]:
                    v_top[x] = y
                if y < v_bottom[x]:
                    v_bottom[x] = y
            if h_left[y] is None:
                h_left[y] = x
                h_right[y] = x
            else:
                if x < h_left[y]:
                    h_left[y] = x
                if x > h_right[y]:
                    h_right[y] = x

        # count covered buildings
        ans = 0
        for x, y in buildings:
            if v_top[x] > y > v_bottom[x] and h_left[y] < x < h_right[y]:
                ans += 1
        return ans

