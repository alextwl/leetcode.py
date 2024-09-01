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


'''
oneliner ver
'''


class Solution:
    def construct2DArray(self, orig: List[int], m: int, n: int) -> List[List[int]]:
        return [] if len(orig) != m * n else [orig[n*i:n*(i+1)] for i in range(m)]


'''
oneliner + new bulit-in func in python 3.12
'''


class Solution:
    def construct2DArray(self, orig: List[int], m: int, n: int) -> List[List[int]]:
        return [] if len(orig) != m * n else list(itertools.batched(orig, n=n))

