'''
2025/11/04 daily challenge

counter + sorting approach
'''


import collections


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        def get_xsum(ctr):
            arr = sorted(ctr.items(), key=lambda v: (v[1], v[0]), reverse=True)[:x]
            return sum(k * fq for k, fq in arr)

        ctr = collections.Counter(nums[:k])
        ans = [get_xsum(ctr)]
        left = 0
        for right in range(k, len(nums)):
            ctr[nums[left]] -= 1
            ctr[nums[right]] += 1
            ans.append(get_xsum(ctr))
            left += 1
        return ans

