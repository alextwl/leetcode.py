'''
2023/03/25 daily challenge

depth first search approach
'''

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        if n == 1:
            return 0
        
        graph = [set() for _ in range(n)]
        for a, b in edges:
            graph[a].add(b)
            graph[b].add(a)

        visited = [False] * n

        def dfs(node):
            '''
            if node was visited, return 0, otherwise return 1 and continue searching.
            '''
            if visited[node]:
                return 0
            
            visited[node] = True
            counts = 1
            for child in graph[node]:
                counts += dfs(child)
            return counts

        group_nodes = []  # each element indicates a group's node counts
        for i in range(n):
            if cnt := dfs(i):
                group_nodes.append(cnt)
        
        # calculate pairs of nodes that are unreachable from each other
        ans = 0
        prev = group_nodes.pop()
        remaining_sum = sum(group_nodes)
        while(group_nodes):
            ans += remaining_sum * prev
            prev = group_nodes.pop()
            remaining_sum -= prev

        return ans

