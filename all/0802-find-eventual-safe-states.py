'''
2023/07/12 daily challenge

Kahn's algorithm + breadth first search approach

learnt from official solution
https://leetcode.com/problems/find-eventual-safe-states/solution/

reverse the graph and run Kahn's algorithm to filter acyclic part of nodes.
'''

import collections


class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)

        # rebuild and reverse the graph
        g = [list() for _ in range(n)]  # g[a] = {b} is a -> b in reversed direction
        indegree = [0] * n
        for i, nodes in enumerate(graph):
            for adj in nodes:
                g[adj].append(i)  # reversed
                indegree[i] += 1
        
        # BFS
        q = collections.deque()
        # initial zero-indegree nodes are safe nodes, start searching from these nodes.
        for i, incomings in enumerate(indegree):
            if incomings == 0:
                q.append(i)
        
        # remove outgoing edges from zero-indegree nodes iteratively
        while(q):
            node = q.popleft()
            for adj in g[node]:
                indegree[adj] -= 1
                if indegree[adj] == 0:
                    # the adjacent node has zero indegree now and can be a safe node, queue it.
                    q.append(adj)

        # return all nodes with zero indegree
        return [i for i, incomings in enumerate(indegree) if incomings == 0]

