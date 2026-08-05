'''
2026/08/05 daily challenge

modified topology sort (actually breadth first search) approach
'''


import collections


class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        indegree = [0] * n

        has_bug = [False] * n
        has_bug[k] = True

        for u, v in invocations:
            g[u].append(v)
            indegree[v] += 1

        q = collections.deque()
        q.append(k)

        while q:
            node = q.popleft()
            for next_hop in g[node]:
                # next_hop tainted by current buggy node
                indegree[next_hop] -= 1
                if not has_bug[next_hop]:
                    q.append(next_hop)
                    has_bug[next_hop] = True

        for flag, deg in zip(has_bug, indegree):
            if flag and deg:
                # there are outsiders (indegree > 0) invoking the method,
                # cannot remove it.
                break
        else:
            # can remove all buggy methods
            return [i for i, flag in enumerate(has_bug) if not flag]

        # cannot remove buggy methods
        return list(range(n))

