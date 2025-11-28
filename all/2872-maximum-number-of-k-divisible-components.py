'''
2024/12/21 daily challenge
2025/11/28 daily challenge

depth first search approach (recursive ver)

search subtrees and count edges we can cut.
'''


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        g = {i: set() for i in range(n)}
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

        def dfs(node, parent = None):
            sum_val = values[node]
            sum_cuts = 0
            for child in g[node] - {parent}:
                val, cuts = dfs(child, node)
                if val % k:
                    sum_val += val
                    sum_cuts += cuts
                else:
                    sum_cuts += cuts + 1
            return (sum_val, sum_cuts)

        return dfs(0)[1] + 1


'''
breadth first search approach

BFS from bottom level and remove edges from leaves.

learnt from official solution 2:
https://leetcode.com/problems/maximum-number-of-k-divisible-components/solution/
'''


import collections


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1

        g = {i: set() for i in range(n)}
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        
        # BFS from leaves (node with only one edge to parent)
        q = collections.deque(node for node, neighbors in g.items() if len(neighbors) == 1)
        ans = 0
        while q:
            node = q.popleft()
            next_node = g[node].pop() if g[node] else -1
            if next_node >= 0:
                g[next_node].remove(node)
            
            if values[node] % k:
                values[next_node] += values[node]
            else:
                ans += 1  # add one more component
            
            # queue the next node if it becomes a leaf
            if next_node >= 0 and len(g[next_node]) == 1:
                q.append(next_node)

        return ans


'''
topological sort approach

add remainder to all neighbors if current node value was indivisible.
'''


import collections


class Solution:
    def maxKDivisibleComponents(self, n: int, edges: List[List[int]], values: List[int], k: int) -> int:
        if n < 2:
            return 1

        g = {i: set() for i in range(n)}
        indegree = [0] * n
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
            indegree[a] += 1
            indegree[b] += 1

        ans = 0
        q = collections.deque(i for i, v in enumerate(indegree) if v == 1)
        while q:
            curr = q.popleft()
            indegree[curr] -= 1

            # value to be added to neighbors
            # if current node was indivisible by k
            adds = 0
            if (rem := values[curr] % k):
                adds = rem
            else:
                # one more valid component found
                ans += 1

            for adj in g[curr]:
                if indegree[adj] == 0:
                    continue
                indegree[adj] -= 1

                if adds:
                    values[adj] += adds

                if indegree[adj] == 1:
                    q.append(adj)

        return ans

