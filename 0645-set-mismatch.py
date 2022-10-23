'''
2022/10/23 daily challenge

XOR approach

learnt from official solution.

the idea is to find a way to reduce the problem,
and cancel all num by XOR except the duplicate one and the missing one.
'''

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        xor = xor0 = xor1 = 0
        
        '''
        try to XOR the entire nums and 1~len(nums) together,
        and the missing can't get cancelled,
        so the resultant xor will be
        == the duplicate one XOR the missing one.
        
        e.g.
        
        (1^2^2^4) ^ (1^2^3^4)
        
        = 2^3
        
        = duplicate_num ^ missing_num.
        '''
        for n in nums:
            xor ^= n
        for i in range(1, len(nums) + 1):
            xor ^= i
        
        '''
        calculate the right most '1' bit.
        it preserves only the first '1' bit from the rightmost.
        '''
        rmb = xor & ~(xor-1)
        
        '''
        divide the nums[] into 2 parts where
        xor0[] contains num without rmb,
        xor1[] contains num with rmb.
        
        if the duplicate num was in xor0, the missing one is in xor1,
        or conversely duplicate_num in xor1, missing_num in xor0.
        
        hint: the rmb bit indicates there's a bit where
        duplicate_num and missing_num's bit must be different,
        so we have a chance to reduce the problem and
        split the array by rmb into 2 parts
        which contain duplicate_num & missing_num separately.
        '''
        for n in nums:
            if (n & rmb) != 0:
                xor1 ^= n
            else:
                xor0 ^= n
        
        '''
        divide the serial array (1~n) into 2 parts in the same way.
        
        the num from the serial array will cancel all values of nums[]
        from xor0 & xor1 except duplicate_num & missing_num.
        '''
        for i in range(1, len(nums) + 1):
            if (i & rmb) != 0:
                xor1 ^= i
            else:
                xor0 ^= i
        
        '''
        if xor0 was in the original nums[], xor0 is duplicate_num.
        if xor0 wasn't in nums[], xor0 is missing_num.
        '''
        for i in range(len(nums)):
            if nums[i] == xor0:
                return [xor0, xor1]
        
        return [xor1, xor0]
