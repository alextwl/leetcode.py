'''
2023/08/26 daily challenge

greedy + dp approach
'''

import collections


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        '''
        sort by right node in ascending order
        '''
        pairs.sort(key=lambda x:x[1])
        
        last_node = -1001  # a value smaller than the input range
        '''
        so when we iterate pairs,
        we can proceed only if the left node of current pair
        is greater than last right node, and extend the chain length.
        '''
        chain_length = 0
        for left, right in pairs:
            if left > last_node:
                chain_length += 1
                last_node = right

        return chain_length


'''
dynamic programming approach
'''

import collections


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        n = len(pairs)
        '''
        sort by each left node of pair
        '''
        pairs.sort()
        
        '''
        the max depth of each pair as a terminal
        '''
        dp = [1] * n
        
        '''
        bottom-up iteration
        '''
        for i in range(n-1, -1, -1):
            for j in range(i+1, n):
                '''
                for any pairs[i] -> pairs[j] which left of j must be greater than right of i.
                '''
                if pairs[i][1] < pairs[j][0]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


'''
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

