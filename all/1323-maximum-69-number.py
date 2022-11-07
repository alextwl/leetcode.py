'''
2022/11/07 daily challenge

conversion approach

change the rightmost 6 to 9 or do nothing.
'''

class Solution:
    def maximum69Number (self, num: int) -> int:
        return int(str(num).replace('6','9',1))

