'''
bitwise approach
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # cancel all duplicate first.
        x1 = 0

        for v in nums:
            x1 ^= v

        '''
        we have x1 = ans1 ^ ans2,
        and we can know at least a bit is different between ans1 & ans2.

        find that bit where it occured first.
        '''
        pos = 0
        while(pos < 32):
            if (x1 >> pos) & 1:
                break
            pos += 1

        '''
        XOR all numbers with that bit set to find ans1.
        it will cancel all duplicates, include only ans1 and exclude ans2.
        '''
        ans1 = 0
        mask = 1 << pos
        for v in nums:
            if v & mask:
                ans1 ^= v

        '''
        we've found ans1.
        
        cancel ans1 from x1 so that we can get ans2.
        '''
        ans2 = x1 ^ ans1

        return [ans1, ans2]

