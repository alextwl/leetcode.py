'''
2024/06/12 daily challenge
2025/05/17 daily challenge

counting sort approach
'''


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        counts = [nums.count(0), nums.count(1), 0]
        counts[2] = len(nums) - counts[0] - counts[1]

        i = 0
        for color in range(3):
            for _ in range(counts[color]):
                nums[i] = color
                i += 1
        return

