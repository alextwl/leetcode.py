'''
2023/10/18 daily challenge

topological sort approach
'''

import collections


class Solution:
    def minimumTime(self, n: int, relations: List[List[int]], time: List[int]) -> int:
        g = [[] for _ in range(n+1)]
        indegree = [0] * (n+1)
        maxtime = [0] * (n+1)

        # v -> w
        for v, w in relations:
            g[v].append(w)
            indegree[w] += 1

        # build a queue with terminal nodes (the courses without prerequisites)
        q = collections.deque()
        for i, indegree_val in enumerate(indegree):
            if indegree_val == 0:
                q.append(i)
                # set the base cost (time) of a node
                maxtime[i] = time[i-1]  # note the input time list is 0-indexed

        # remove dummy index 0
        q.popleft()
        maxtime[0] = 0

        # topological sort
        while q:
            node = q.popleft()
            for parent in g[node]:
                # update the parent's max cost
                maxtime[parent] = max(maxtime[parent], maxtime[node] + time[parent-1])
                indegree[parent] -= 1
                if indegree[parent] == 0:
                    q.append(parent)

        return max(maxtime)

