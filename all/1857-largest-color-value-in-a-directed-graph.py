'''
2023/04/09 daily challenge

Topological sorting (zero indegree) approach

See Kahn's algorithm:
https://en.wikipedia.org/wiki/Topological_sorting#Kahn's_algorithm
'''


class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        cnum = [ord(c) - ord('a') for c in colors]

        # build graph
        graph = {i: set() for i in range(n)}
        node_indegrees = [0] * n  # each node's indegrees (== the count of edge destinated to the node)
        for a, b in edges:
            graph[a].add(b)
            node_indegrees[b] += 1

        # initiate counter for each node with its color counted.
        node_counter = [[0] * 26 for _ in range(n)]
        for i, init_color in enumerate(cnum):
            node_counter[i][init_color] = 1
        # filter nodes with zero indegree
        zero_indegree_nodes = set(i for i, indegree in enumerate(node_indegrees) if indegree == 0)

        largest = 0
        visited_count = 0
        while(zero_indegree_nodes):
            node = zero_indegree_nodes.pop()
            # visit the node, only nodes where we start traversing from can be visited.
            visited_count += 1
            for child in graph[node]:
                # merge each color's max value to the child
                for c in range(26):
                    if cnum[child] == c:
                        # grow the color c's value from current counter if it's bigger than the child's
                        # if the child's color is also the c. (== concatenate the path from the node/parent)
                        node_counter[child][c] = max(node_counter[child][c], node_counter[node][c] + 1)
                    else:
                        node_counter[child][c] = max(node_counter[child][c], node_counter[node][c])
                # remove the node as a parent of child (decrease the indegree)
                node_indegrees[child] -= 1
                if node_indegrees[child] == 0:
                    '''
                    no more parents to the child,
                    we can add it into the set of zero indegree nodes
                    and visit it in the next while-loop.
                    '''
                    zero_indegree_nodes.add(child)
            # update the largeest color value with the current counter's maximum value
            largest = max(largest, max(node_counter[node]))

        if visited_count != n:
            '''
            all nodes should be visited (where start traversing from) once exactly,
            if there's a loop, nodes in that loop cannot have zero indegree and they cannot be visited.
            '''
            return -1

        return largest

