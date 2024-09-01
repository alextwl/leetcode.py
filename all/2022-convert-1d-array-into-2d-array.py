'''
2024/09/01 daily challenge
'''


class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []

        ans = []
        it = iter(original)
        for _ in range(m):
            row = []
            for _ in range(n):
                row.append(next(it))
            ans.append(row)

        return ans

