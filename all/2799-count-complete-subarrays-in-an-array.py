'''
2025/04/24 daily challenge

sliding window approach

learnt from official editorial:
https://leetcode.com/problems/count-complete-subarrays-in-an-array/editorial/

note subarrays with same elements but different positions also count respectively.
'''


import collections


class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        cnt = dict()

        ans = 0
        distincts = len(set(nums))
        right = 0
        for left in range(n):
            if left:
                rm = nums[left - 1]
                cnt[rm] -= 1
                if cnt[rm] == 0:
                    cnt.pop(rm)
            
            while right < n and len(cnt) < distincts:
                add = nums[right]
                cnt[add] = cnt.get(add, 0) + 1
                right += 1
            
            if len(cnt) == distincts:
                ans += n - right + 1
        return ans

