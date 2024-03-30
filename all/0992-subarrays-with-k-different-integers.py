'''
2024/03/30 daily challenge

sliding window approach

similar to problem 2958 but the idea is

f_WithKDistinct(k) == f_WithAtMostKDistinct(k) - f_WithAtMostKDistinct(k - 1)
'''


import collections


class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def getMostKDistinct(nums: List[int], k: int):
            freq = collections.defaultdict(int)
            count = 0
            left = 0

            for right, right_val in enumerate(nums):
                freq[right_val] += 1

                # note the function counts the number of subarrays
                # with at most k distinct elements,
                # **NOT** at most k frequency of any element.
                while (len(freq) > k):
                    freq[nums[left]] -= 1
                    if freq[nums[left]] == 0:
                        # so we need to remove the key
                        # if the element no longer included
                        del freq[nums[left]]
                    left += 1

                count += right - left + 1

            return count

        return getMostKDistinct(nums, k) - getMostKDistinct(nums, k - 1)

