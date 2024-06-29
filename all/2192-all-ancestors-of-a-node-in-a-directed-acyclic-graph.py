'''
2024/06/29 daily challenge

topological sort approach
'''

import collections


class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        indegrees = [0] * n
        children = {i: set() for i in range(n)}
        
        for u, v in edges:
            indegrees[v] += 1
            children[u].add(v)
        
        q = collections.deque()
        for i, ind in enumerate(indegrees):
            if ind == 0:
                q.append(i)
        
        ancestors = [list() for _ in range(n)]
        
        while(q):
            node = q.popleft()
            ancestors[node] = sorted(set(ancestors[node]))

            for child in children[node]:
                ancestors[child].append(node)
                ancestors[child].extend(ancestors[node])
                indegrees[child] -= 1
                if indegrees[child] == 0:
                    q.append(child)

        return ancestors

