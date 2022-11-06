'''
dynamic programming + go forward approach

memorize the maximum accumulated jump length and compare it to the index.

space=O(1)
'''

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        jumped = 0  # max jumped length
        
        for position, jump in enumerate(nums):
            if position > jumped:
                # we can never jump to here
                return False
            
            '''
            if `jumped` was bigger, current position is bypassed,
            otherwise we can jump further from here. (== position + jump)
            '''
            jumped = max(jumped, position + jump)
        
        # last index reached
        return True
