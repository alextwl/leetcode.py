'''
2023/09/30 daily challenge

stack approach

learnt from official solution 4
https://leetcode.com/problems/132-pattern/solution/

p.s. comments lets leetcode.com return HTTP 403 when running or submitting code.
remove all comment blocks before submission.
'''

class Solution:
    def find132pattern(self, nums) -> bool:
        n = len(nums)
        if n < 3:
            return False

        '''
        build an array where each index i has a minimum of nums[0..i]
        '''
        min_i = float('inf')
        min_array = []
        for v in nums:
            min_i = min(min_i, v)
            min_array.append(min_i)
        
        '''
        a stack for tracking seen elements in reversed order
        '''
        stack = []
        
        for j in range(n-1, -1, -1):
            jv = nums[j]
            min_i = min_array[j]
            
            if jv <= min_i:
                # 2 (a value of j) <= 1 (min_i), miss.
                continue
            while stack and stack[-1] <= min_i:
                # 1 (min_i) >= 3 (top of stack as a value of k), miss.
                # try to pop and find if there's an occurance of 1 < 2.
                stack.pop()
            '''
            so we found 1 < 2 and no case for 1 >= 3 now.
            '''
            if stack and stack[-1] < jv:
                '''
                3 < 2 matched, we found the 132 pattern.
                (1 < 2 and not(1 >= 3) and 3 < 2) == 1 < 3 < 2.
                '''
                return True
            stack.append(jv)

        return False

