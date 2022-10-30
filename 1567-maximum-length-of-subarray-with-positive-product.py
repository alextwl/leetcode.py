'''
dynamic programming approach

track positive & negative number counters by dp.
'''

class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        max_len = 0
        '''
        pos_count = the length of current subarray ended with positive product.
        neg_count = the length of current subarray ended with negative product.
        '''
        pos_count = neg_count = 0
        
        for num in nums:
            if num == 0:
                # reset counts
                pos_count = neg_count = 0
            elif num > 0:
                pos_count += 1
                '''
                iterated negative numbers may be also part of current subarray, so we need to increment it if existed.
                '''
                neg_count = neg_count + 1 if neg_count > 0 else 0
            else:  # num < 0
                '''
                neg_count > 0 means there's already a negative number, so -value * -value = +value.
                the last negative product length +1 will be new pos_count.
                if neg_count == 0, it cannot form a subarray with positive product so assign zero to pos_count.
                
                for neg_count, the subarray tracked by pos_count becomes negative because of num<0,
                so assign pos_count +1 to neg_count.
                '''
                pos_count, neg_count = neg_count + 1 if neg_count > 0 else 0, pos_count + 1

            max_len = max(max_len, pos_count)

        return max_len
