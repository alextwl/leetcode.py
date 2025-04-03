'''
2025/04/03 daily challenge

greedy method approach

same to problem 2873 but come with bigger input, brute-force won't work.
'''


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        ans = max_i = max_i_j = 0
        for v in nums:
            ans = max(ans, (max_i_j) * v)
            max_i_j = max(max_i_j, max_i - v)
            max_i = max(max_i, v)
        return ans

