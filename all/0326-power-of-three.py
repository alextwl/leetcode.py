'''
2025/08/13 daily challenge
'''


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        
        while(n % 3 == 0):
            n = n // 3
        
        return n == 1


'''
loop with early returns
'''


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        while n > 1:
            n, rem = divmod(n, 3)
            if rem:
                return False
        return True

