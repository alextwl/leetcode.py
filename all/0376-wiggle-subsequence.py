'''
dynamic programming approach

learnt from official solution.

time=O(n**2), space=O(n)
'''

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        '''
        2 dp arrays for i-th element as the last element of subsequence &
        ending witl a rising/falling (up/down) wiggle.
        
        each element can be also a length-1 wiggle subsequence.
        '''
        up = [1] * n
        down = up.copy()
        
        for i in range(1, n):
            for j in range(0, i):
                '''
                the idea is finding a longest wiggle sequence
                consisting of s[0:j+1] + s[i].
                we just consider s[0]..s[j] + s[i] but not k-th elements between j < k < i.
                (we can consider some bypassed k-th elements as deleted from wiggle subseqs.)
                
                it tries to expand the longest wiggle subseq from s[0:j+1] + s[i] to s[0:i].
                
                if neither the following conditions are true,
                nums[j] will be considered as deleted.
                '''
                if nums[i] > nums[j]:
                    up[i] = max(up[i], down[j] + 1)
                elif nums[i] < nums[j]:
                    down[i] = max(down[i], up[j] + 1)

        return max(up[-1], down[-1])

