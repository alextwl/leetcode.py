'''
2024/06/28 daily challenge

sorting by degree approach
'''


class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        for u, v in roads:
            degrees[u] += 1
            degrees[v] += 1
        return sum(i * ind for i, ind in enumerate(sorted(degrees), start=1))

