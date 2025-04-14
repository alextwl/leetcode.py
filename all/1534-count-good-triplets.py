'''
2025/04/14 daily challenge

exhaustive method approach

time=O(n**3)
'''


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        ans = 0

        for i, x in enumerate(arr):
            for j in range(i + 1, n):
                y = arr[j]
                if abs(x - y) > a:
                    continue
                for k in range(j + 1, n):
                    z = arr[k]
                    if abs(y - z) <= b and abs(x - z) <= c:
                        ans += 1
        return ans


'''
optimized prefix approach

learnt from official editorial 2:
https://leetcode.com/problems/count-good-triplets/editorial/#approach-2-optimized-enumeration

time=O(n**2 + 1000n)
'''


class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)

        ans = 0
        # prefix_i[x] = accumulated counts of arr[i] in [0:x]
        prefix_i = [0] * 1001

        for j, y in enumerate(arr):
            for k in range(j + 1, n):
                z = arr[k]
                if abs(y - z) > b:
                    continue
                # convert |x - y| <= a to x in [y - a, y + a]
                min_x0, max_x0 = y - a, y + a
                # convert |x - z| <= c to x in [z - c, z + c]
                min_x1, max_x1 = z - c, z + c
                # find the intersection of [y - a, y + a] & [z - c, z + c],
                # remember to exclude y - a < 0 and z + c > 1000 cases.
                min_x, max_x = max(0, min_x0, min_x1), min(1000, max_x0, max_x1)
                if min_x <= max_x:
                    if min_x == 0:
                        ans += prefix_i[max_x]
                    else:
                        # note min_x is included, so we subtract min_x-1 counts
                        ans += prefix_i[max_x] - prefix_i[min_x - 1]
            # reuse the arr[j] loop as enumerating [x:1000], accumulate the prefix counts >= arr[x].
            for x in range(y, 1001):
                prefix_i[x] += 1
        return ans

