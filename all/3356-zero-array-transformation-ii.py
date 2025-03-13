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


'''
line sweeping approach

learnt from official editorial 2:
https://leetcode.com/problems/zero-array-transformation-ii/editorial/#approach-2-line-sweep

iterate through nums and apply enough queries to difference array.
'''


class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        k = 0  # the counter of applied queries
        diff = [0] * (len(nums) + 1)
        delta = 0
        m = len(queries)

        for i, v in enumerate(nums):
            # apply queries until nums[i] equals zero
            while v > delta + diff[i]:
                # apply next query to the difference array
                k += 1
                if k > m:
                    return -1

                a, b, w = queries[k-1]
                # no need to proceed the query if its range was prior to nums[i].
                if b >= i:
                    diff[max(a, i)] += w
                    diff[b+1] -= w
            delta += diff[i]
        return k

