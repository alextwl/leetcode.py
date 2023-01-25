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

