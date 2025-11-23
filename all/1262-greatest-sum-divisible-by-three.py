'''
2025/11/23 daily challenge

sorting + math approach

if sum(nums) % 3 had a remainder:

    1: need to remove another remainder one 1 or two 2
    2: need to remove another remainder one 2 or two 1

pick the greater result between above modes
'''


class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        mod = total % 3
        if not mod:
            return total

        nums.sort()
        ans0 = ans1 = 0
        if mod == 1:
            # need another remainder one 1 or two 2
            mod2 = 0
            for v in nums:
                rem = v % 3
                if not rem:
                    continue
                if rem == 1:
                    if not ans0:
                        ans0 = total - v
                else:
                    # rem == 2:
                    if not ans1:
                        if mod2:
                            ans1 = total - mod2 - v
                        else:
                            mod2 = v
                if ans0 and ans1:
                    break
        else:
            # need another remainder one 2 or two 1
            mod1 = 0
            for v in nums:
                rem = v % 3
                if not rem:
                    continue
                if rem == 2:
                    if not ans0:
                        ans0 = total - v
                else:
                    # rem == 1
                    if not ans1:
                        if mod1:
                            ans1 = total - mod1 - v
                        else:
                            mod1 = v
                if ans0 and ans1:
                    break
        if not ans0 and not ans1:
            return 0
        return max(ans0, ans1)

