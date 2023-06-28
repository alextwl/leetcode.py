'''
2023/06/28 daily challenge

Dijkstra + max heap approach
'''

import collections
import heapq


class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        '''
        for a <-> b with a probability p,
        graph[a] = [(b, p), ...]
        graph[b] = [(a, p), ...]
        
        the values of graph default to list because
        there may be multiple edges between 2 nodes.
        '''
        graph = collections.defaultdict(list)
        for edge, p in zip(edges, succProb):
            a, b = edge
            graph[a].append((b, p))
            graph[b].append((a, p))
        
        # the minimum negatived (because we wanna use max heap) probability of each node.
        probs = [0.0] * n
        probs[start] = -1.0
        
        '''
        use max heap as queue, ordered by negatived probability.
        '''
        h = [(-1.0, start)]
        while(h):
            path_p, node = heapq.heappop(h)
            
            '''
            the end point has the maximum probability among traversed nodes,
            there's no more path with greater probability because each edge's
            maximum probability is limited to <= 1.
            '''
            if node == end:
                return -path_p

            for next_node, next_p in graph[node]:
                new_path_p = next_p * path_p
                if new_path_p < probs[next_node]:
                    probs[next_node] = new_path_p
                    heapq.heappush(h, (new_path_p, next_node))
        
        # we cannot find a path from start to end.
        return 0.0

