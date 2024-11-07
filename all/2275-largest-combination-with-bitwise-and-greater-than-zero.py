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


'''
space optimized & speed up ver
'''


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        max_cnt = 0
        for mask in [1 << i for i in range(24)]:
            count = 0
            for v in candidates:
                if v & mask:
                    count += 1
            max_cnt = max(max_cnt, count)
        return max_cnt

