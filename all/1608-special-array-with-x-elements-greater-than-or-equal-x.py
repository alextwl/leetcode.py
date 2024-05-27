'''
2024/05/27 daily challenge

sorting approach
'''


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(reverse=True)

        prev = -1
        for i, v in enumerate(nums, start=1):
            if v == prev:
                continue

            if i > v:
                if prev >= i - 1 and i - 1 != v:
                    return i - 1
                return -1

            prev = v

        if nums[-1] >= n:
            return n

        return -1

