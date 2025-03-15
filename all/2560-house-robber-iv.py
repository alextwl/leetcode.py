'''
2025/03/15 daily challenge

binary search approach
'''


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def validate(cap):
            # check if we could rob k houses with specific capability
            prev = 1_000_000_007
            seq_len = 0
            for v in nums:
                if v <= cap:
                    if prev <= cap:
                        # skip adjacent house
                        prev = 1_000_000_007
                    else:
                        seq_len += 1
                        if seq_len == k:
                            return True
                        prev = v
                else:
                    prev = v
            return False
        
        l, r = min(nums), max(nums)
        while l < r:
            mid = (l + r) // 2
            if validate(mid):
                r = mid
            else:
                l = mid + 1
        return l

