'''
2024/11/27 daily challenge

breadth first search approach
'''


import collections


class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        # build the graph following the definition of problem
        g = [[i+1] for i in range(0, n - 1)]
        g.append([])  # for n-1 node

        # minimum distance from node 0 to node i
        min_dist = [i for i in range(n)]

        ans = []

        last_node = n - 1
        for u, v in queries:
            g[u].append(v)
            
            # BFS
            q = collections.deque()
            # try to reiterate only node v with (maybe) shorter path length
            q.append((min_dist[u] + 1, v))
            while q:
                path_len, node = q.popleft()
                if path_len >= min_dist[node]:
                    continue
                min_dist[node] = path_len
                if node == last_node:
                    continue
                # search deeper
                path_len += 1
                for next_node in g[node]:
                    q.append((path_len, next_node))
            ans.append(min_dist[-1])

        return ans

