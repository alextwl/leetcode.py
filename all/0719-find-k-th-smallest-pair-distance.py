'''
2024/08/14 daily challenge

bucket sort approach (TLE)
'''


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        max_num = max(nums)
        
        buckets = [0] * (max_num + 1)
        
        for i, ival in enumerate(nums):
            for j in range(i + 1, n):
                dist = abs(ival - nums[j])
                buckets[dist] += 1
        
        for dist, cnt in enumerate(buckets):
            k -= cnt
            if k <= 0:
                return dist
        
        return -1  # undefined behavior


'''
sliding window + binary search approach (AC)
'''


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        
        def count_pairs(max_dist):
            cnt = 0
            i = 0
            
            for j, jval in enumerate(nums):
                while jval - nums[i] > max_dist:
                    i += 1
                cnt += j - i
            return cnt

        # binary search
        left, right = 0, nums[-1] - nums[0]
        while left < right:
            mid = (left + right) >> 1
            rank = count_pairs(mid)

            if rank < k:
                left = mid + 1
            else:
                right = mid

        return left

