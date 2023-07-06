'''
2023/07/06 daily challenge

sliding window approach
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        psum = 0  # current subarray sum
        plen = 0  # current subarray length

        min_plen = float('inf')

        left_iter = iter(nums)

        for rnum in nums:
            psum += rnum
            plen += 1

            if target <= psum:
                min_plen = min(min_plen, plen)

                # try to shrink the subarray
                for lnum in left_iter:
                    psum -= lnum
                    plen -= 1
                    if target <= psum:
                        min_plen = min(min_plen, plen)
                    else:
                        # the subarray sum is smaller than target, no need to shrink more
                        break

        return 0 if min_plen == float('inf') else min_plen

