'''
brute force + prefix sum-like approach

runtime=1373ms, Beats 11.55%
'''


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        # last_pos[val] = the index of nums where its value is equal or smaller than val.
        last_pos = [-1] * 1001
        for i, v in enumerate(nums):
            last_pos[v] = i
        prev_pos = -1
        for i in range(1001):
            if last_pos[i] == -1:
                last_pos[i] = prev_pos
            else:
                prev_pos = last_pos[i]

        # skip zero lengths
        start = 0
        while start < n and nums[start] == 0:
            start += 1

        # O(n**2) search for the 1st & 2nd elements of a triplet
        ans = 0
        for i in range(start, n - 2):
            v0 = nums[i]
            for j in range(i + 1, n - 1):
                two_sum = v0 + nums[j]
                ans += max(j, last_pos[min(1000, two_sum - 1)]) - j
        return ans

