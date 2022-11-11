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


'''
better dynamic programming approach (linear ver)

learnt from official solution.

time=O(n), space=O(2n)
'''

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = [0] * n
        down = up.copy()
        up[0] = down[0] = 1
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                # nums[i] is added to the rising sequence (expands previous falling sequence.)
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                # nums[i] is added to the falling sequence (expands previous rising sequence.)
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                # nums[i] is deleted (bypassed) from the sequences
                up[i], down[i] = up[i-1], down[i-1]

        return max(up[-1], down[-1])


'''
extreme dynamic programming approach (space-optimized ver)

learnt from official solution.

time=O(n), space=O(1)
'''

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        up = down = 1
        
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                # nums[i] is added to the rising sequence (expands previous falling sequence.)
                up = down + 1
            elif nums[i] < nums[i-1]:
                # nums[i] is added to the falling sequence (expands previous rising sequence.)
                down = up + 1
            '''
            else:
                # nums[i] is deleted (bypassed) from the sequences
                pass
            '''
        return max(up, down)

