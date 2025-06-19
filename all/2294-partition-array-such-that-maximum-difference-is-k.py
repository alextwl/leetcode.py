'''
2025/06/19 daily challenge

greedy method approach
'''


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        min_val = nums[0]
        seq_count = 1
        for v in nums:
            if v - min_val > k:
                min_val = v
                seq_count += 1
        return seq_count

