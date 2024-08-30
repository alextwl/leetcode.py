'''
2024/08/30 daily challenge

Dijkstra's algorithm approach

try to add each negative-weight edge,
rerun Dijkstra's algorithm multiple times,
and see if we can find a path with target distance.
'''


import heapq


class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        g = {i: dict() for i in range(n)}
        
        for a, b, w in edges:
            if w > -1:
                g[a][b] = w
                g[b][a] = w
        
        def get_shortest_pathlen():
            min_lens = [math.inf] * n
            min_lens[source] = 0
            
            h = [(0, source)]  # min heap: (pathlen, node)
            
            while(h):
                pathlen, node = heapq.heappop(h)
                
                if pathlen > min_lens[node]:
                    continue
                
                for next_hop, w in g[node].items():
                    if (new_pathlen := pathlen + w) < min_lens[next_hop]:
                        min_lens[next_hop] = new_pathlen
                        heapq.heappush(h, (new_pathlen, next_hop))

            return min_lens[destination]
        
        shortest = get_shortest_pathlen()
        if shortest < target:
            # graph without negative-weight edges has path shorter than target.
            return []
        
        if shortest == target:
            # graph without negative-weight edges already has target shortest path.
            for edge in edges:
                # find all negative edges and override it with irrelevant weight
                if edge[2] == -1:
                    edge[2] = 1_000_000_001  # assign a weight larger than input range
            return edges
        
        # try to add each negative-weight edge
        for i, (a, b, w) in enumerate(edges):
            if w != -1:
                continue
            
            # start from weight-1
            edges[i][2] = 1
            g[a][b] = 1
            g[b][a] = 1
            
            new_shortest = get_shortest_pathlen()
            
            if new_shortest <= target:
                # adjust weight and add all remaining difference to the edge
                edges[i][2] += target - new_shortest
                
                # no need to use remaining negative-weight edges, override them.
                for j in range(i+1, len(edges)):
                    if edges[j][2] == -1:
                        edges[j][2] = 1_000_000_001
                return edges
        # the destination is unreachable
        return []

