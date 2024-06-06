'''
counter + O(2n) loops approach

learnt from problem 846's official solution 2 'reverse decrement'

same as 846 Hand of Straights
'''


import collections


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k:
            return False
        
        ctr = collections.Counter(nums)
        
        for v in nums:
            # find the first number
            first = v
            while ctr[first - 1]:
                first -= 1
            
            # try to group from the first number
            while first <= v:
                # there may be multiple 'first' number, try to exhaust it by grouping.
                # if it's already exhausted, bypass it.
                while ctr[first]:
                    for next_num in range(first, first + k):
                        if not ctr[next_num]:
                            # insufficient unused number
                            return False
                        ctr[next_num] -= 1
                first += 1

        return True

