'''
2024/11/07 daily challenge

count the appearance of each bit and find the max.
'''


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        cnt = {i: 0 for i in range(24)}  # max 10**7
        for v in candidates:
            i = 0
            while v:
                if v & 1:
                    cnt[i] += 1
                v >>= 1
                i += 1
        return max(cnt.values())

