'''
2022/09/21 daily challenge
'''

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        '''
        calculate the sum of even values first.
        '''
        evens = sum([num for num in nums if not num & 1])
        ans = []
        
        # time to query
        for qval, qindex in queries:
            orig_num = nums[qindex]
            if not orig_num & 1:
                # always subtract original num if it's even.
                evens -= orig_num
            
            # apply the query
            num_val = orig_num + qval
            nums[qindex] = num_val
            
            if not num_val & 1:
                # add the sum if num+val==even
                evens += num_val
            
            # print the answer
            ans.append(evens)
        
        return ans
