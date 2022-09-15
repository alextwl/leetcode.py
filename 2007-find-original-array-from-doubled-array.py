'''
2022/09/15 daily challenge
'''

'''
counter hashmap ver
learnt from
https://leetcode.com/problems/find-original-array-from-doubled-array/discuss/1485450/Python-hashmap-O(n)-solution.-NO-Sorting!

it looks like time=O(n**2), but since each value is visited at most 3 times, time=O(3n)=O(n).
'''

import collections

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) & 1:
            # an array with odd length is definitely not a doubled array.
            return []
        counter = collections.Counter(changed)
        ans = []
        
        for val in counter.keys():
            if val == 0:
                # handle special case 0
                if counter[0] & 1:
                    # not a doubled array if array had odd number of zeroes.
                    return []
                # append half number of zeroes as original values to answer array
                ans += [0] * (counter[0] >> 1)
                
            elif counter[val]:
                # find the smallest odd divisor of the value first
                # because any even divisor may be also an doubled value of other original value
                d = val
                while not (d & 1) and (d >> 1) in counter:
                    d = d >> 1
                
                while d in counter:
                    if counter[d]:
                        if counter[d << 1] < counter[d]:
                            # if the number of doubled value is smaller than the original's,
                            # it means at least one original has no its doubled value,
                            # the doubled array does not exist.
                            return []
                        # original value found
                        # append half number of vals to original array
                        ans += [d] * counter[d]
                        # remove counts of both originals and doubles
                        counter[d << 1] -= counter[d]
                        counter[d] = 0
                    # search doubled value if it's also an original value of other doubled value
                    d = d << 1
        
        return ans

'''
intuitive ver, time limit exceeded
'''

class Solution2:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) & 1:
            # an array with odd length is definitely not a doubled array.
            return []
        
        changed.sort()
        ans = []
        
        while(changed):
            # the smallest value is always a value of original array.
            original = changed[0]
            del changed[0]
            doubled = original << 1
            
            for idx, val in enumerate(changed):
                if val == doubled:
                    # doubled value found
                    ans.append(original)
                    del changed[idx]
                    break
                elif val > doubled:
                    # doubled value not found
                    return []
            else:
                # doubled value not found
                return []
        
        return ans
