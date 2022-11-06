'''
2022/09/23 daily challenge

intuitive ver
'''

class Solution:
    def concatenatedBinary(self, n: int) -> int:
        modulo = 10**9 + 7
        ans = 0
        
        for x in range(1, n+1):
            '''
            1. shift the number of length of x in binary form.
               len(bin(x)) - 2 == len(bin(x)[2:])
            2. since shifted bits were zeroed in default, add x to write shifted bits.
            3. apply modulo
            '''
            ans = ((ans << (len(bin(x)) - 2)) + x) % modulo
        
        return ans
