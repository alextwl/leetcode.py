# 2022/08/05 daily challenge

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = dict()
        dp[0] = 1
        
        def search(subtar: int) -> int:
            if subtar < 0:
                return 0
            if subtar in dp:
                return dp[subtar]
            comb_sum = 0
            for num in nums:
                if subtar > num:
                    comb_sum += search(subtar-num) # search sub-set of combination subtracted by num.
                elif subtar == num:
                    comb_sum += 1  # count 1 if subtar can be constructed only by num.
            dp[subtar] = comb_sum
            return comb_sum
            
        return search(target)
