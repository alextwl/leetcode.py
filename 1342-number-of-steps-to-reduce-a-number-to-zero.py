class Solution:
    def numberOfSteps(self, num: int) -> int:
        ''' intuitive
        step = 0
        while (num):
            step += 1
            num = num -1 if (num & 1) else num >> 1
        return step
        '''
        ''' bit manipulation'''
        binstr = bin(num)[2:]
        step = len(binstr) + binstr.count('1') - 1
        return step
