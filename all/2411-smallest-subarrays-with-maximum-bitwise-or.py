'''
2025/07/29 daily challenge

bitwise + pointer approach

memorize the last seen position of each bit reversely.
'''


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos = [0] * 30
        ans = []

        for i in range(n - 1, -1, -1):
            v = nums[i]
            j = 0
            while v:
                if v & 1:
                    pos[j] = i
                j += 1
                v >>= 1
            ans.append(max(max(pos), i) - i + 1)

        ans.reverse()
        return ans

