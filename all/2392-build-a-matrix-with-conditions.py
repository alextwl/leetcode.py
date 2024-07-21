'''
2024/07/21 daily challenge

Kahn's algorithm + topology sort approach

learnt from official solution 2:
https://leetcode.com/problems/build-a-matrix-with-conditions/solution/
'''


import collections


class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topology_sort(edges, n):
            adj = [[] for _ in range(n+1)]
            indegree = [0] * (n+1)
            order = []
            
            for a, b in edges:
                adj[a].append(b)
                indegree[b] += 1

            # init with leaves
            q = collections.deque([i for i, deg in enumerate(indegree) if deg == 0])
            q.popleft()  # remove dummy zero, keep 1..k only
            while q:
                a = q.popleft()
                order.append(a)
                n -= 1
                
                for b in adj[a]:
                    indegree[b] -= 1
                    if indegree[b] == 0:
                        q.append(b)
            if n != 0:
                return []
            return order
        
        order_rows = topology_sort(rowConditions, k)
        order_cols = topology_sort(colConditions, k)
        
        if not order_rows or not order_cols:
            return []
        
        ans = [[0] * k for _ in range(k)]
        for i, v1 in enumerate(order_rows):
            for j, v2 in enumerate(order_cols):
                if v1 == v2:
                    ans[i][j] = v1
        return ans

