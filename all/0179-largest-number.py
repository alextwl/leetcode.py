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

