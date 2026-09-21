'''
2026/09/21 daily challenge

modular arithmetic + dynamic programming approach
'''


class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        rem_ctr = [0] * k  # number of ways of each remainder

        dp0 = [0] * k
        for i, v in enumerate(nums):
            # proceed all subarrays starting from nums[i]
            dp1 = [0] * k
            v_rem = v % k
            dp1[v_rem] = 1

            # modulo distributive property:
            # prev_product * v = curr_product
            # ((prev_product % k) * (v % k)) % k = (prev_rem * curr_rem) % k
            for rem, prev in enumerate(dp0):
                dp1[(rem * v_rem) % k] += prev

            # accumulate to ans
            for rem, curr in enumerate(dp1):
                rem_ctr[rem] += curr

            dp0 = dp1

        return rem_ctr

