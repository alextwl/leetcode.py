'''
2022/11/16 daily challenge

binary search approach
'''

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        
        while(left <= right):
            mid = left + (right-left)//2
            result = guess(mid)
            if result == 0:
                return mid
            elif result == 1:
                # the answer is in the right.
                left = mid + 1
            elif result == -1:
                # the answer is in the left.
                right = mid - 1
            else:
                #raise NotImplementedError('undefined behavior.')
                return -1

        return -1

