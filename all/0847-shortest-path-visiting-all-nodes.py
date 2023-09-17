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


'''
level order search approach (simplified BFS)

the minimum level with all nodes visited is the answer,
and we don't need to search deeper.
'''

import collections


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        full_mask = 2**n - 1  # the mask indicating all nodes are visited.
        
        level = 0
        
        # (node, visited_mask)
        q = collections.deque([(i, 1 << i) for i in range(n)])
        
        # dp[i] = set of seen visited_mask at i-th node.
        dp = [set() for _ in range(n)]
        
        while(q):
            level_len = len(q)
            
            for _ in range(level_len):
                node, visited_mask = q.popleft()
                
                if visited_mask in dp[node]:
                    continue
                
                dp[node].add(visited_mask)
                
                if visited_mask == full_mask:
                    return level
                
                # queue children
                for child in graph[node]:
                    q.append((child, visited_mask | (1 << child)))
            
            # goto next level
            level += 1
        
        # undefined behavior: the question guarantees the input graph is always connected.
        # this should not be happened.
        return float('inf')

