'''
2024/07/26 daily challenge

min heap approach (runtime=7135 ms)
'''

import heapq


class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        g = {i: dict() for i in range(n)}
        for a, b, w in edges:
            if w <= distanceThreshold:
                g[a][b] = w
                g[b][a] = w
        
        min_neighbor = 101
        ans = -1
        for start in range(n):
            visited_set = {start}
            h = [(0, start)]  # min heap: (path_len, node)
            while h:
                path_len, node = heapq.heappop(h)
                
                for child, w in g[node].items():
                    new_path_len = path_len + w
                    if new_path_len > distanceThreshold or \
                            child == start or \
                            new_path_len > g[start].get(child, float('inf')):
                        continue
                    g[start][child] = new_path_len
                    g[child][start] = new_path_len
                    heapq.heappush(h, (new_path_len, child))
                    visited_set.add(child)
                if min_neighbor != 101 and len(visited_set) > min_neighbor:
                    break
            if min_neighbor == 101 or len(visited_set) < min_neighbor:
                min_neighbor = len(visited_set)
                ans = start
                #print("init min=%d, ans=%d" % (min_neighbor, ans))
            elif len(visited_set) == min_neighbor:
                ans = max(ans, start)
                #print("update min=%d, ans=%d" % (min_neighbor, ans))

        return ans

