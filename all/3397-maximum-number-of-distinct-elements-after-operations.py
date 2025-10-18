'''
2025/10/18 daily challenge

greedy method approach

learnt from official editorial:
https://leetcode.com/problems/maximum-number-of-distinct-elements-after-operations/editorial/#approach-greedy
'''


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()

        prev = float('-inf')
        ans = 0
        for v in nums:
            # choose smallest valid number
            # in the range of [v - k, v + k] and also next to prev until (v + k).
            curr = min(max(v - k, prev + 1), v + k)
            if curr > prev:
                # if too many numbers were in the current range,
                # curr will eventually hit (v + k) multiple times and also == prev.
                ans += 1
                prev = curr
        return ans

