'''
2026/06/26 daily challenge

optimized prefix sum approach

learnt from official editorial:
https://leetcode.com/problems/count-subarrays-with-majority-element-ii/editorial/#approach-prefix-sum
'''


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        pfx = [0] * (n * 2 + 1)  # counter of seen prefix sums: -n, -n+1, ..., 0, ..., n-1, n
        pfx[n] = 1  # there's one base case for prefix sum==0

        ans = 0
        pos = n  # the index (current prefix sum) of pfx array, starts from n (for sum==0)
        curr_sum = 0
        for i, v in enumerate(nums):
            if v == target:
                # if nums[i] == target, add 1 to prefix sum
                curr_sum += pfx[pos]

                pos += 1
                pfx[pos] += 1
            else:
                # if nums[i] != target, subtract 1 from prefix sum
                pos -= 1
                curr_sum -= pfx[pos]

                pfx[pos] += 1

            ans += curr_sum

        return ans

