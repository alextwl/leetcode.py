'''
2025/06/28 daily challenge

sorting approach
'''


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        srt = sorted(((i, v) for i, v in enumerate(nums)), 
                     key=lambda x: (x[1], x[0]), reverse=True)
        ans = []
        for _, v in sorted(srt[:k]):
            ans.append(v)
        return ans

