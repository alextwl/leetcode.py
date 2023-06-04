'''
leetcode 75 lv2 day 19

Union-Find approach
'''

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        uf = dict()

        def find(city):
            if uf.setdefault(city, city) != city:
                uf[city] = find(uf[city])
            return uf[city]
        
        def union(city1, city2):
            '''
            group city1 & city2 into the same province.
            '''
            capital1, capital2 = find(city1), find(city2)
            # smallest index of a city is the capital of the province.
            if capital1 < capital2:
                uf[capital2] = capital1
            else:
                uf[capital1] = capital2
        
        n = len(isConnected)
        for i in range(n):
            for j in range(i, n):
                if i != j and isConnected[i][j]:
                    union(i, j)
        
        provinces = set()
        for i in range(n):
            provinces.add(find(i))

        return len(provinces)


'''
2023/06/04 daily challenge

Union-Find approach (rank ver)
'''


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = dict()
        rank = dict()

        def find(x):
            if parent.setdefault(x, x) != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            x, y = find(x), find(y)
            if rank.setdefault(x, 0) >= rank.setdefault(y, 0):
                rank[x] += 1
                parent[y] = x
            else:
                rank[y] += 1
                parent[x] = y

        for i in range(n):
            for j in range(i+1, n):
                if isConnected[i][j]:
                    union(i, j)

        provinces = set()
        for i in range(n):
            provinces.add(find(i))

        return len(provinces)

