'''
2025/06/01 daily challenge

enumeration (brute-force) approach

learnt from official solution 1:
https://leetcode.com/problems/distribute-candies-among-children-ii/editorial/#approach-1-enumeration
'''


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(limit, n) + 1):
            if (j := n - i) > limit * 2:
                continue
            ans += min(j, limit) - max(0, j - limit) + 1
        return ans

