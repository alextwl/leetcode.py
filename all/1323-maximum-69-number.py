'''
2022/11/07 daily challenge

conversion approach

change the rightmost 6 to 9 or do nothing.
'''

class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6','9',1))


'''
arithmetic approach

divide num by 10 recursively and memorize the last remainder of 6,
add the difference of maximum number to the original input, and then return it.
'''

class Solution:
    def maximum69Number (self, num: int) -> int:
        quo = num
        
        left = 0  # index from leftmost.
        right6 = None  # index of last seen '6'
        while (quo > 0):
            quo, rem = divmod(quo, 10)
            if rem == 6:
                right6 = left
            left += 1
        
        if right6 is not None:
            '''
            return the maximum number.
            
            e.g. 9699 + 3 * 10 ** 2 = 9699 + 300 = 9999
            '''
            return num + 3 * 10**right6

        # 6 not found, do nothing.
        return num

