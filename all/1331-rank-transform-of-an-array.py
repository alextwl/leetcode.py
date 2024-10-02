'''
2024/10/02 daily challenge

sorting approach
'''


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        num2rank = {v: i for i, v in enumerate(sorted(set(arr)), start=1)}
        return [num2rank[v] for v in arr]

