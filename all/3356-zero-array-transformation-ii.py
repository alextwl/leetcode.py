'''
2025/03/13 daily challenge

binary search approach
'''


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        def validate(k):
            n = len(nums)
            diff = [0] * (n + 1)  # difference array

            for idx in range(k):
                a, b, v = queries[idx]
                diff[a] += v
                diff[b+1] -= v
            
            delta = 0
            for v, w in zip(nums, diff):
                delta += w
                if v > delta:
                    return False
            return True
        
        n = len(nums)
        l, r = 0, len(queries)
        # try to apply all queries first.
        if not validate(r):
            return -1
        
        while l <= r:
            mid = (l + r) // 2
            if validate(mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

