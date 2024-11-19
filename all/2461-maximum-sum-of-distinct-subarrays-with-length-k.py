'''
2024/11/19 daily challenge

hash + sliding window approach
'''


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0

        left = 0
        last_seen = dict()
        curr_sum = 0

        for right, v in enumerate(nums):
            if last_seen.get(v, -1) >= left:
                for i in range(left, last_seen[v] + 1):
                    curr_sum -= nums[i]
                left = last_seen[v] + 1

            last_seen[v] = right
            curr_sum += v

            if (right - left + 1) == k:
                max_sum = max(max_sum, curr_sum)
                curr_sum -= nums[left]
                left += 1

        return max_sum

