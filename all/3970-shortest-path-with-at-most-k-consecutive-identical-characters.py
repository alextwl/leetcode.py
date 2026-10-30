'''
2026/10/30 daily challenge

shortest path approach (Dijkstra's algorithm)
'''


import heapq


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        end = n - 1
        g = [[] for _ in range(n)]  # g[u][v] = weight of u->v
        for u, v, w in edges:
            g[u].append((v, w))

        # min_dist[node][seen_consecutive_count] = minimum distance from 0 to node
        min_dist = [[float('inf')] * (k + 1) for _ in range(n)]
        # min heap: {path_len, node, seen_consecutive_count}
        h = []

        # base case for node 0
        # only one letter also has a length-1 of consecutive identical char.
        min_dist[0][1] = 0
        heapq.heappush(h, (0, 0, 1))

        # Dijkstra's algorithm
        while h:
            path_len, node, cont_len = heapq.heappop(h)
            if path_len > min_dist[node][cont_len]:
                continue
            if node == end:
                return path_len

            curr_char = labels[node]

            for next_hop, w in g[node]:
                if labels[next_hop] == curr_char:
                    # consecutive identical characters continue.
                    next_cont = cont_len + 1
                    if next_cont > k:
                        continue
                else:
                    next_cont = 1

                if (new_path_len := path_len + w) < min_dist[next_hop][next_cont]:
                    min_dist[next_hop][next_cont] = new_path_len
                    heapq.heappush(h, (new_path_len, next_hop, next_cont))

        # destination unreachable
        return -1

