'''
2025/04/02 daily challenge

exhaustive method approach
'''


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i, ival in enumerate(nums):
            for j in range(i + 1, n - 1):
                i_j = ival - nums[j]
                for k in range(j + 1, n):
                    kval = nums[k]
                    if i_j ^ kval < 0:
                        continue
                    ans = max(ans, i_j * kval)
        return ans


'''
greedy method approach
'''


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        max_i = 0
        max_i_j = 0
        ans = 0

        for v in nums:
            # assume the current value is nums[k],
            # we have a value of triplet max(previous nums[i]-nums[j]) * nums[k].
            ans = max(ans, max_i_j * v)
            # assume the current value is nums[j],
            # try to maximize (previous max(nums[i]) - nums[j]) for further use.
            max_i_j = max(max_i_j, max_i - v)
            # assume the current value is nums[i],
            # maximize nums[i] for further use.
            max_i = max(max_i, v)

        return ans

