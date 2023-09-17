'''
2023/09/17 daily challenge

breadth first search + bitmasking + dynamic programming approach

since n <= 12, it's possible to start iterating from all nodes in brute force.
'''

import collections


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        full_mask = 2**n - 1  # the mask indicating all nodes are visited.
        
        ans = float('inf')

        dp = collections.defaultdict(lambda: float('inf'))
        
        # start BFS from each node
        for root in range(n):
            q = collections.deque()
            q.append((0, 0, root))  # (path_len, visited_mask, node)

            # BFS
            while(q):
                path_len, visited_mask, node = q.popleft()
                
                # visit the node
                visited_mask |= 1 << node

                if visited_mask == full_mask:
                    ans = min(ans, path_len)
                    continue

                # check if the length of path exceeded the previous result
                if path_len >= ans or path_len >= dp[(visited_mask, node)]:
                    # no need to search further
                    continue

                dp[(visited_mask, node)] = path_len

                # queue children
                path_len += 1
                for child in graph[node]:
                    # always queue all children because
                    # revisiting nodes multiple times is allowed.
                    q.append((path_len, visited_mask, child))

        return ans

