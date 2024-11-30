'''
2024/11/30 daily challenge

Hierholzer's algorithm approach (find an Euler circuit)
'''

import collections
import itertools


class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:
        g = collections.defaultdict(list)
        in_deg = collections.defaultdict(int)
        out_deg = collections.defaultdict(int)

        for a, b in pairs:
            g[a].append(b)
            out_deg[a] += 1
            in_deg[b] += 1

        # find the head node
        head = -1
        for node, cnt in out_deg.items():
            if cnt == in_deg[node] + 1:
                head = node
                break
        else:
            # start from the first pair's start node if previous criteria not found
            head = pairs[0][0]

        circuit = []
        stack = [head]

        # DFS
        while stack:
            # backtrace previous visited node in the path and forward to any unused edge
            node = stack[-1]
            if g[node]:
                stack.append(g[node].pop())
            else:
                # no more unused edge from node, add the node to the Euler circuit
                circuit.append(node)
                stack.pop()

        # reverse the circuit and rebuild rearranged pairs
        ans = [[a, b] for a, b in itertools.pairwise(reversed(circuit))]
        return ans

