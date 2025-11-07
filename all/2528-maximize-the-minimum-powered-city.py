'''
2025/11/07 daily challenge

difference array + binary search approach

learnt from official editorial:
https://leetcode.com/problems/maximize-the-minimum-powered-city/editorial/#approach-binary-search--difference-array

binary search the largest minimum powered city.

validate target power and add extra power plant from k by greedy method.
'''


class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        n = len(stations)

        diff = [0] * (n + 1)
        for i, curr in enumerate(stations):
            diff[max(i - r, 0)] += curr  # left inclusive
            diff[min(i + r + 1, n)] -= curr  # right exclusive

        def validate(target):
            # validate if we can have target minimum power
            arr = diff.copy()
            cnt = 0  # counter of current powers
            rem_k = k

            for i in range(n):
                # assume i is the left boundary of window r*2
                cnt += arr[i]
                if cnt < target:
                    # power lower than target, add extra plants.
                    extra = target - cnt
                    rem_k -= extra
                    if rem_k < 0:
                        # insufficient extra power plant
                        return False
                    # diff next to the right boundary
                    arr[min(i + r * 2 + 1, n)] -= extra
                    cnt += extra
            return True
        
        left, right = min(stations), sum(stations) + k
        ans = 0
        while left <= right:
            mid = (left + right) >> 1
            if validate(mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        return ans

