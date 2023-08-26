'''
2023/08/26 daily challenge

depth first search approach

it's slow and nearly timed out.
'''

import collections


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        '''
        # convert pairs to unidirectional graph
        [left, right] = left -> right
        '''
        g = collections.defaultdict(set)
        for a, b in pairs:
            g[a].add(b)
        
        '''
        the last seen max depth of a vertex
        '''
        max_depth = collections.defaultdict(int)
        
        stack = [(node, 1) for node in sorted(g, reverse=True)]  # (node, depth)
        while(stack):
            node, depth = stack.pop()
            if max_depth[node] >= depth:
                # the current route does not make a longer chain, skipping.
                continue
            
            # update maximum depth of the node as a terminal
            max_depth[node] = depth
            
            # queue all possible destinations
            depth += 1
            min_right = min(g[node])
            stack.extend([(t, depth) for t in g.keys() if t > min_right])

        return max(max_depth.values())

