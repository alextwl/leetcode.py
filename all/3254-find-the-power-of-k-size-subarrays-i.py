'''
2024/11/16 daily challenge

counter approach
'''


import itertools


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        ans = []
        sub_len = 1
        for i, (v0, v1) in enumerate(itertools.pairwise(nums), start=2):
            if v0 + 1 == v1:
                if sub_len < k:
                    sub_len += 1
                if sub_len == k:
                    # the maximum element is always the last element in the current subarray
                    ans.append(v1)
                elif i >= k:
                    ans.append(-1)
            else:
                sub_len = 1  # reinitialize the subarray starting at here.
                if i >= k:
                    ans.append(-1)

        return ans

