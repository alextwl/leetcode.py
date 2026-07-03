'''
2026/07/03 daily challenge

binary search + shortest path (Dijkstra's algorithm) approach
'''


import heapq


class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        n1 = n - 1  # destination
        g = [[] for _ in range(n)]

        left, right = float('inf'), 0
        # build a directed graph
        for u, v, w in edges:
            if not online[u] or not online[v]:
                # one of terminals is offline node, skip this edge
                continue
            # u -> v with w cost
            g[u].append((v, w))
            # update search range
            left = min(left, w)
            right = max(right, w)
        
        def is_path_valid_w(target_score):
            h = [(0, 0)]  # (path distance, node)
            distances = [float('inf')] * n
            distances[0] = 0

            while h:
                dist, curr = heapq.heappop(h)
                if dist > k:
                    return False
                if curr == n1:
                    # a valid path found
                    return True
                if dist > distances[curr]:
                    continue
                
                for next_hop, w in g[curr]:
                    if w < target_score:
                        # smaller than targeted maximum path score (mid), skip
                        continue
                    if distances[next_hop] > (new_dist := distances[curr] + w):
                        distances[next_hop] = new_dist
                        heapq.heappush(h, (new_dist, next_hop))
            # path not found
            return False
        
        # must have a path with score equal or bigger than lowest weight edge
        if not is_path_valid_w(left):
            return -1
        
        while left <= right:
            mid = (left + right) // 2
            if is_path_valid_w(mid):
                left = mid + 1
            else:
                right = mid - 1

        return right

