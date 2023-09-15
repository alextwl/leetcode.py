'''
minimum spanning tree (MST) question

Kruskal's Algorithm + Union-Find approach
'''


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        '''
        calculate manhattan distances between all pairs of any two points.
        '''
        def getDistance(x1, y1, x2, y2):
            return abs(x1-x2) + abs(y1-y2)

        edges = []
        
        for i, i_point in enumerate(points):
            for j in range(i+1, n):
                j_point = points[j]
                
                dist = getDistance(*i_point, *j_point)
                edges.append((dist, i, j))
        
        '''
        Union-find structure
        '''
        parent = [i for i in range(n)]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            '''
            union x & y and return whether they were already united or not.
            '''
            x, y = find(x), find(y)
            if x == y:
                return True
            
            if x > y:
                parent[x] = y
            else:
                parent[y] = x
            
            return False
        
        '''
        Kruskal's Algorithm
        
        sort the edges by distance, and add edges into Union-Find structure in increasing order.
        '''
        edges.sort(key=lambda x:x[0])
        
        # there are at most n-1 edges to form an MST with n points.
        mstEdgeCount = 0
        mstMaxSize = n - 1
        
        mstMinCost = 0

        for dist, i, j in edges:
            if not union(i, j):
                # add this edge to MST.
                mstMinCost += dist
                mstEdgeCount += 1
            
            if mstEdgeCount == mstMaxSize:
                # all points were in the MST
                return mstMinCost
        
        # there's only one point with no edges.
        return 0


'''
2023/09/15 daily challenge

Prim's algorithm + heap approach
'''

import heapq


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)

        '''
        calculate manhattan distances between all pairs of any two points.
        '''
        def getDistance(x1, y1, x2, y2):
            return abs(x1-x2) + abs(y1-y2)

        ans = 0  # minimum cost
        seen = set()  # a set of visited vertices
        '''
        a min heap ordered by (manhattan distance, from, to)
        start from the first point to itself with zero distance.
        (so that we can visit it and iterate all connections to other vertices.)
        '''
        h = [(0, 0, 0)]
        
        # iterate until all points visited
        while(len(seen) < n):
            dist, _, u = heapq.heappop(h)
            
            if u in seen:
                # already visited
                continue

            seen.add(u)

            # add the distance which is the minimum manhattan distance
            # from the current heap
            ans += dist

            # iterate all connections from u to other vertices.
            for v in range(n):
                if v not in seen:
                    heapq.heappush(h,
                                   (getDistance(*points[u], *points[v]), u, v))

        return ans

