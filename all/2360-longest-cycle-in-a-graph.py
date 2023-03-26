'''
2023/03/26 daily challenge

depth first search approach

note that each node has **at most one** outgoing edge,
that means each node joins **at most one** cycle

we can visit each node once only and skip those visited
and no need to worry if any longer cycles started there.
'''


class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        firstdepth = [float('inf')] * n  # each node's first seen depth
        visited = set()

        def dfs(node, depth):
            if edges[node] == -1:
                # the traversal ends at a terminal, no cycle starts here.
                return -1

            if node in visited:
                return -1

            if depth > firstdepth[node]:
                # a cycle is detected here, get the diff
                return depth - firstdepth[node]
            
            # this is the first 
            firstdepth[node] = depth

            # traverse the next node
            diff = dfs(edges[node], depth+1)
            '''
            if it's done before traversing deeper,
            we couldn't find a cycle because the cycle's starting node would be tagged.
            so we tag the node as visited here.
            '''
            visited.add(node)

            return diff
        
        longest = -1
        for i in range(n):
            longest = max(longest, dfs(i, 0))
        
        return longest

