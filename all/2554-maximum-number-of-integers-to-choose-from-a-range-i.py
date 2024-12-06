'''
2024/12/06 daily challenge

set + linear search approach
'''


class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        banned = set(banned)
        curr_sum = 0
        ans = 0
        
        for v in range(1, n + 1):
            if v in banned:
                continue
            curr_sum += v
            if curr_sum > maxSum:
                break
            ans += 1

        return ans

