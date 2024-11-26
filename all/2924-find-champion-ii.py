'''
2024/11/26 daily challenge

find if there's only one zero-indegree node
'''


class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        indegree = [0] * n
        for _, b in edges:
            indegree[b] += 1

        champion = -1
        for i, cnt in enumerate(indegree):
            if cnt == 0:
                if champion != -1:
                    return -1
                champion = i

        return champion

