'''
2024/09/18 daily challenge

heap + custom comparative function approach

learnt from official solution 4:
https://leetcode.com/problems/largest-number/solution/
'''

import heapq


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        class CustomStr(str):
            def __lt__(self, other):
                return other + self < self + other

        h = []
        for v in nums:
            heapq.heappush(h, CustomStr(v))
        result = []
        while h:
            result.append(heapq.heappop(h))

        if result[0] == "0":
            return "0"
        
        return ''.join(result)


'''
custom quicksort approach
'''


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        
        def qsort(arr):
            if len(arr) < 2:
                return arr
            
            pivot_idx = len(arr) // 2
            pivot_val = arr[pivot_idx]
            
            lefts, rights = list(), list()
            
            for i, s in enumerate(arr):
                if i == pivot_idx:
                    continue
                # the comparsion is reversed because we want a descending list.
                if s + pivot_val < pivot_val + s:
                    rights.append(s)
                else:
                    lefts.append(s)
            
            return qsort(lefts) + [pivot_val] + qsort(rights)

        ans = ''.join(qsort(nums))
        
        return "0" if ans[0] == '0' else ans

