'''
2026/01/22 daily challenge

brute-force method approach

same to problem 3510.
'''


class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        def is_sorted():
            for a, b in itertools.pairwise(nums):
                if a > b:
                    return False
            return True
        
        removal = 0
        while not is_sorted():
            min_sum = float('inf')
            target = None
            for i in range(len(nums) - 1):
                if (pair_sum := nums[i] + nums[i+1]) < min_sum:
                    min_sum = pair_sum
                    target = i
            nums[target] = min_sum
            nums.pop(target + 1)
            removal += 1

        return removal

