'''
2025/04/16 daily challenge

two pointers approach
'''


import collections


class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        n = len(nums)
        cnt = collections.defaultdict(int)
        pair_cnt = 0
        ans = 0

        right = -1
        for left, lv in enumerate(nums):
            # extend right pointer if insufficient pairs
            while pair_cnt < k and (next_right := right + 1) < n:
                right = next_right
                rv = nums[right]
                # if there already had same values of nums[right],
                # we can form the same amount of pairs with the current nums[right].
                pair_cnt += cnt[rv]
                cnt[rv] += 1
            if pair_cnt >= k:
                ans += n - right
            # shrink window
            cnt[lv] -= 1
            pair_cnt -= cnt[lv]

        return ans

