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

