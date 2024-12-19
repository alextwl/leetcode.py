'''
2024/12/19 daily challenge

counter approach
'''


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cnt0 = [0] * 10
        cnt1 = cnt0.copy()

        chunks = 0
        for v0, v1 in zip(arr, sorted(arr)):
            cnt0[v0] += 1
            cnt1[v1] += 1
            if cnt0 == cnt1:
                chunks += 1

        return chunks

