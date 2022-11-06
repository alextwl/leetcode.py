'''
2022/08/19 daily challenge

learnt from
https://leetcode.com/problems/split-array-into-consecutive-subsequences/discuss/106514/C%2B%2BPython-Esay-Understand-Solution
'''
import collections

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        counts = collections.Counter(nums)  # remaining count of num to be proceeded
        end = collections.Counter()  # counts sequences end at num
        # end also uses Counter(). when a num was not an end of any sequence, it returns zero instead of raises KeyError.
        
        for num in nums:
            if not counts[num]:
                # the num has been added to a certain sequence.
                continue
            
            counts[num] -= 1
            
            if end[num-1] > 0 :
                # find a sequence (which can append num) ends at num-1
                end[num-1] -= 1
                end[num] += 1
            elif counts[num+1] > 0 and counts[num+2] > 0:
                # find if it's possible to form a sequence of length 3
                # by num & 2 bigger nums. ([num, num+1, num+2])
                # it works only for the condition:
                # Each subsequence is a consecutive increasing sequence
                # (i.e. each integer is exactly one more than the previous integer).
                counts[num+1] -= 1
                counts[num+2] -= 1
                end[num+2] += 1
            else:
                # Impossible to append num to any sequence
                return False
        
        return True
