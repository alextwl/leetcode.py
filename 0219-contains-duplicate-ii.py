'''
2022/10/21 daily challenge

pop slow number when fast > k >= (fast - slow).
'''

import collections

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        c = collections.Counter()
        slow = fast = 0
        
        for num in nums:
            if fast > k:
                c[nums[slow]] = 0
                slow += 1
            fast += 1

            if c[num]:
                return True
            else:
                c[num] = 1
        
        return False

'''
evict slow number by set. (runtime slower than dict)
'''

class Solution2:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        s = set()
        slow = fast = 0
        
        for num in nums:
            if fast > k:
                s.remove(nums[slow])
                slow += 1
            fast += 1
            
            if num in s:
                return True
            else:
                s.add(num)
        
        return False
