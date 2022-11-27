'''
2022/11/27 daily challenge

depth first search approach (brute force, TLE)
'''

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def dfs(inum: int, seq: List[int]) -> int:
            '''
            generate all possible subsequences by adding or skipping nums[inum].
            
            :param inum: the index of num in nums[] to be included in the subsequence or not.
            :param seq: the current subsequence.
            '''
            if inum == len(nums):
                '''
                check the arithmetic attribute only when we traversed the nums[].
                (so that we have all possible subsequences.)
                we may check it every time but it's also too time-consuming.
                '''
                if len(seq) < 3:
                    '''
                    a sequence lesser than 3 numbers is not arithmetic by definition.
                    no need to check.
                    '''
                    return 0
                for i in range(1, len(seq)):
                    # verify if it's arithmetic
                    if (seq[i] - seq[i-1]) != (seq[1] - seq[0]):
                        return 0
                # it is a valid arithmetic subsequence.
                return 1
            
            '''
            the sequence without nums[inum] goes left.
            (we need to feed it a copy of seq so that it does not mess up with right side's seq.)
            '''
            left = dfs(inum + 1, seq.copy())
            seq.append(nums[inum])
            # the sequence **with** nums[inum] goes right.
            right = dfs(inum + 1, seq)
            
            return left + right
        
        # start the dfs from the beginning of nums[] and an empty subsequence.
        return dfs(0, [])


'''
dynamic programming approach

learnt from official solution

the definition of weak arithmetic sequence (nums[i] != nums[j] and len(nums) == 2)
is imported for initializing the common difference parameter of dp
but its count is not included in the answer.
'''

import collections

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        
        '''
        dp[i][diff] = the number of weak arithmetic subsequences
                      ending with nums[i] & diff the common difference.
        '''
        dp = [collections.defaultdict(int) for _ in range(n)]
        
        for i in range(1, n):
            for j in range(0, i):
                diff = nums[i] - nums[j]
                '''
                get the number of existed weak subseqs ending with j as the base value (if it didn't exist it returns zero.)
                and add it (plus one new weak subseq [nums[j], nums[i]]) to dp[i] with the same diff.
                
                dp[i][diff] = existed weak subseqs + all cases of [..., nums[j], nums[i]].
                '''
                total_seq = dp[j][diff]
                dp[i][diff] += total_seq + 1
                
                '''
                we just add dp[j][diff] to answer because we don't want to count the weak part.
                if dp[j][diff] was existed (> 0), it means its existed subseqs are all equal or longer than 2 numbers,
                so appending nums[i] to these subseqs absolutely forms valid arithmetic subsequences consisting of at least 3 numbers.
                '''
                ans += total_seq
        
        return ans

