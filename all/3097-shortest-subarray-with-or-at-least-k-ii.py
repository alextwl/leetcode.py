'''
2024/11/10 daily challenge

sliding window approach
'''


class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        n = len(nums)
        min_len = float('inf')
        bcnt = [0] * 32  # track count of 1's bits at each bit in the length of 32-bit integer

        left = right = 0
        while right < n:
            # accumulate set bit counts for nums[right]
            rval = nums[right]
            for i in range(32):
                if rval & (1 << i):
                    bcnt[i] += 1

            # try to shrink the window from left if the bitwise OR result is >= k.
            while (left <= right and sum(1 << i for i, v in enumerate(bcnt) if v) >= k):
                min_len = min(min_len, right - left + 1)

                # reduce counts by removing nums[left]'s bits
                lval = nums[left]
                for i in range(32):
                    if lval & (1 << i):
                        bcnt[i] -= 1

                left += 1
            right += 1

        return -1 if min_len == float('inf') else min_len

