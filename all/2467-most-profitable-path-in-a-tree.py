'''
2025/02/24 daily challenge

depth first search + breadth first search approach

do DFS for bob, record arrival depth for each node,
and then BFS for alice.
'''


import collections


class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n = len(amount)
        g = [list() for _ in range(n)]
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        
        # find bob's path
        bob_visited_time = [-1] * n
        def dfs(src_node, depth):
            nonlocal bob_visited_time
            bob_visited_time[src_node] = depth

            # reached the target: node 0
            if src_node == 0:
                return True
            
            depth += 1
            for adj in g[src_node]:
                if bob_visited_time[adj] == -1:
                    if dfs(adj, depth):
                        return True
            # reset src_node if bob isn't reached node 0 via src_node
            bob_visited_time[src_node] = -2  # visited but not considered
            return False

        dfs(bob, 0)

        # BFS for alice
        max_ans = float('-inf')  # alice may be in debt
        q = collections.deque([[0, 0, 0]])  # src, time(depth), money
        visited = set()
        while q:
            src, depth, money = q.popleft()
            if bob_visited_time[src] < 0 or depth < bob_visited_time[src]:
                # alice arrives src before bob
                money += amount[src]
            elif depth == bob_visited_time[src]:
                # alice and bob arrive at the same time
                money += amount[src] >> 1
            # else: alice gets no money

            # update ans only if it's a leaf
            if src != 0 and len(g[src]) == 1:
                max_ans = max(max_ans, money)
            
            depth += 1
            for adj in g[src]:
                if adj not in visited:
                    q.append([adj, depth, money])

            visited.add(src)

        return max_ans

