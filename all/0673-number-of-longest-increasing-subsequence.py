'''
2023/07/21 daily challenge

dynamic programming approach

learnt from official solution
https://leetcode.com/problems/number-of-longest-increasing-subsequence/solution/
'''


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        # lis_length[i] = the length of LIS ended at nums[i]
        lis_length = [1] * n
        # lis_count[i] = the count of LIS ended at nums[i]
        lis_count = [1] * n
        
        # O(n**2) nested loops
        for i in range(n):
            for j in range(i):
                '''
                check if nums[i] can append to nums[j]
                '''
                if nums[j] < nums[i]:
                    '''
                    and try to make a longer increasing subsequence
                    '''
                    if (new_len := lis_length[j] + 1) > lis_length[i]:
                        lis_length[i] = new_len
                        '''
                        a longer increasing subsequence is built,
                        previous count of shorter subseqs must be discarded.
                        '''
                        lis_count[i] = 0
                    '''
                    accumulate the LIS count from nums[j] if nums[i] could be appended
                    because all subseqs ended at nums[j] can be extended to nums[i].
                    '''
                    if new_len == lis_length[i]:
                        lis_count[i] += lis_count[j]
        
        max_length = max(lis_length)  # get final LIS length
        ans = 0

        '''
        filter only LIS counts and sum up.
        '''
        for l, c in zip(lis_length, lis_count):
            if l == max_length:
                ans += c

        return ans

