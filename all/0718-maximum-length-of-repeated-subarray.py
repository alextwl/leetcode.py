'''
2022/09/20 daily challenge

learnt from official approach 3:
dynamic programming
'''

class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        dp[i][j] == longest common prefix of nums1[i:] & nums2[j:]
        
        do not init space with `dp = [[0] * B] * A` because inner list will be the same instance for all dp[i].
        '''
        dp = [[0] * (len(nums2)+1) for _ in range(len(nums1) + 1)]
        
        '''
        when nums1[i] == nums2[j],
        dp[i][j] = dp[i+1][j+1] + 1.
        (it's always satisfied even when nums1[i+1] != nums2[j+1] because dp[i+1][j+1] = 0)
        so let's memorize the LCP length reversely.
        '''
        for i in range(len(nums1)-1, -1, -1):
            for j in range(len(nums2)-1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i+1][j+1] + 1
        
        return max(max(dp_i) for dp_i in dp)
