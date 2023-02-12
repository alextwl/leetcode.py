'''
2023/02/12 daily challenge

depth first search approach
'''

import collections
import math


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        # build a bidirectional graph of roads
        graph = collections.defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)

        liters = 0  # total liters of fuel used

        def dfs(city, parent):
            nonlocal liters
            cars = 0
            total_people = 1  # the current city has a representative
            
            for next_city in graph[city] - {parent}:
                people = dfs(next_city, city)
                cars += math.ceil(people / seats)
                # rearrange carpooling for the parent city
                total_people += people
            
            # each car from all next_city to current city costs 1 liter of fuel
            liters += cars

            return total_people
        
        # traverse from the capital (root) city.
        dfs(0, -1)

        return liters

