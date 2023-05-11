'''
2023/05/11 daily challenge

dynamic programming programming
'''


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        let nums1 be equal to or longer than nums2 for the convenience.
        '''
        n1, n2 = len(nums1), len(nums2)
        if n2 > n1:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1
        
        '''
        dp[i][j] = the maximum number of connecting lines between nums1[:i] and nums2[:j]
        '''
        dp = [[0] * (n2+1) for _ in range(n1+1)]

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if nums1[i-1] == nums2[j-1]:
                    '''
                    if i-th nums1 == j-th nums2,
                    the max number of uncrossed lines is
                    (the result of nums1[:i-1] & nums[:j-1]) + 1 the current line.
                    '''
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    '''
                    if the pair could not be connected,
                    inherit the result from either
                    (1) nums1[:i-1] & nums2[:j], or
                    (2) nums1[:i] & nums2[:j-1].
                    '''
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[-1][-1]

