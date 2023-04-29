'''
2023/04/29 daily challenge

Union find approach

the key is to build union-find structure during the processing of those queries
by ascending limits & weights.

when we are processing a query with a limit,
we only add edges which are strictly less than the limit to the union-find structure,
and then we can safely verify the query by evaluating find(u)==find(v).
'''

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        # union-find structure
        parent = [i for i in range(n)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            x, y = find(x), find(y)
            if x > y:
                parent[x] = parent[y]
            else:
                parent[y] = parent[x]

        ans = [None] * len(queries)
        sorted_edges = sorted(edgeList, key=lambda x:x[2])  # sort by ascending distance.
        i = 0  # the index of next edge to be proceeded.
        len_edgeList = len(edgeList)

        # process the query ordered by its limit.
        for j, k in sorted(enumerate(queries), key=lambda x:x[1][2]):
            p, q, limit = k

            # union the vertices by adding edges whose distance lesser than limit.
            while (i < len_edgeList and sorted_edges[i][2] < limit):
                union(sorted_edges[i][0], sorted_edges[i][1])
                i += 1
            
            '''
            Now each edges in the graph of the union-find structures
            has distance lesser than the limit, use find() to check the connectivity.
            '''
            ans[j] = find(p)==find(q)

        return ans

