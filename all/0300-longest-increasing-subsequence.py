# 2022/08/08 daily challenge
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        greedy + linear search ver
        '''
        sub = list()
        for idx, num in enumerate(nums):
            if not sub or sub[-1] < num:
                # num is bigger than last num of sub,
                # can be appended to sub.
                sub.append(num)
            else:
                # search sub for the first occurence >= num,
                # replace it for smaller space O.
                for subidx, subnum in enumerate(sub):
                    if subnum >= num:
                        sub[subidx] = num
                        break
        return len(sub)
        '''
        intuitive ver
        dynamic programming, time=O(N^2), space=O(N)
        '''
        numslen = len(nums)
        # every sub seq started from any num has initial length of 1.
        dp = [1] * numslen
        for idx in range(numslen):
            for subidx in range(idx):
                if nums[idx] > nums[subidx] and dp[idx] < dp[subidx] + 1:
                    '''
                    if nums[idx] can be the larger than last num (nums[subidx]) of subidx seq
                    and subidx seq can be longer than idx seq,
                    use subidx seq (dp[subidx]) + count one (for num[idx]) = the new dp[idx]
                    '''
                    dp[idx] = dp[subidx] + 1
        return max(dp)

'''
learnt from
https://leetcode.com/problems/longest-increasing-subsequence/discuss/1326308/C%2B%2BPython-DP-Binary-Search-BIT-Solutions-Picture-explain-O(NlogN)
'''
