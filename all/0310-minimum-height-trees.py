'''
2024/04/23 daily challenge

breadth first search approach

run BFS from all leaves and remove it from the tree until remaining nodes <= 2.
'''

import collections


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        g = collections.defaultdict(set)
        degree = [0] * n
        for u, v in edges:
            g[u].add(v)
            g[v].add(u)
            degree[u] += 1
            degree[v] += 1
        
        # queue all leaves
        q = collections.deque(node for node, deg in enumerate(degree) if deg == 1)
        
        # there're at most 2 MHTs if two roots were connected together.
        # no way for n >= 3 MHTs if all nodes were in the same tree.
        while n > 2:
            leaf_count = len(q)
            n -= leaf_count  # remove leaves from the total number of nodes
            
            for _ in range(leaf_count):
                node = q.popleft()
                
                # the leaf has only 1 neighbor because degree == 1, no need to iterate, just pop it.
                neighbor = g[node].pop()

                # decrement only the degree of its neighbors,
                # no need for the node because it's going to be removed
                degree[neighbor] -= 1
                g[neighbor].remove(node)

                # if the neighbor becomes the new leaf, queue it.
                if degree[neighbor] == 1:
                    q.append(neighbor)

        return list(q)

