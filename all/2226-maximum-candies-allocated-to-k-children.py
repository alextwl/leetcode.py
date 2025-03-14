'''
2025/03/14 daily challenge

binary search approach
'''


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def validate(candy):
            if not candy:
                return False
            piles = 0
            for v in candies:
                if v >= candy:
                    piles += v // candy
                    if piles >= k:
                        return True
            return False

        ans = 0
        l, r = 1, max(candies)
        while l <= r:
            mid = (l + r) // 2
            if validate(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

