'''
2024/10/30 daily challenge

dynamic programming + longest increasing/decreasing subsequence (LIS) approach

learnt from official solution 1:
https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/solution/
'''


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
        longest_incs = [1] * n
        longest_decs = [1] * n

        # evaluate the length of longest increasing subsequence ending at each element.
        for i, i_val in enumerate(nums):
            max_len = longest_incs[i]
            for j, j_val, j_longest_incs in zip(range(i), nums, longest_incs):
                if j_val < i_val:
                    max_len = max(max_len, j_longest_incs + 1)
            longest_incs[i] = max_len

        # and then for the longest decreasing subsequence starting from each element.
        for i, i_val in reversed(list(enumerate(nums))):
            max_len = longest_decs[i]
            for j in range(i+1, n):
                if i_val > nums[j]:
                    max_len = max(max_len, longest_decs[j] + 1)
            longest_decs[i] = max_len

        ans = float('inf')
        for inc_len, dec_len in zip(longest_incs, longest_decs):
            if inc_len > 1 and dec_len > 1:
                '''
                the minimum removals in the left side of peak
                = (i + 1) - inc_len
                
                the minimum removals in the right side of peak
                = (n - i) - dec_len
                
                add above equations
                = n + 1 - inc_len - dec_len
                '''
                ans = min(ans, n + 1 - inc_len - dec_len)

        return ans

