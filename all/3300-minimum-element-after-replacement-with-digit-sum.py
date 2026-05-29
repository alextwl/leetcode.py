'''
2026/05/29 daily challenge

digit sum conversion by division approach
'''


class Solution:
    def minElement(self, nums: List[int]) -> int:
        min_val = 36  # 9999
        for v in nums:
            digit_sum = 0
            while v:
                v, rem = divmod(v, 10)
                digit_sum += rem
                if digit_sum > min_val:
                    # the sum is already larger than the minimal,
                    # no need to proceed further
                    break
            min_val = min(min_val, digit_sum)
        return min_val

