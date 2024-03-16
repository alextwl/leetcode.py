'''
2024/03/16 daily challenge

counter approach (yet another prefix sum variant)
'''


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        max_len = 0
        count = 0  # relative num of 1's & 0's. (ones - zeros)
        d = {0: -1}  # d[count] = first seen index of num

        for i, v in enumerate(nums):
            count += 1 if v else -1
            if count in d:
                # just like when two prefix sums are equal
                # the sum between these two indexes is zero.
                # since we use the difference between ones and zeros
                # as a kind of prefix sum, a continguous subarray with zero sum
                # is a valid subarray with an equal number of 0 and 1.
                max_len = max(max_len, i - d[count])
            else:
                d[count] = i

        return max_len

