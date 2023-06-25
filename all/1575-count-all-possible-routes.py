'''
2023/06/25 daily challenge

dynamic programming approach (recursive ver)
'''

import functools


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        @functools.cache
        def dfs(city, avail_fuel):
            if avail_fuel < 0:
                return 0

            if city == finish:
                '''
                reached the destination city and there's at least 1 route available,
                if there's remaining fuel, we can continue traversing more cities.
                '''
                routes = 1
            else:
                routes = 0

            current_loc = locations[city]
            for next_city, next_loc in enumerate(locations):
                if next_city == city:
                    # do not immediately revisit the current city
                    continue
                routes = (routes + dfs(next_city,
                                       avail_fuel - abs(current_loc - next_loc))) % 1_000_000_007
            
            return routes

        return dfs(start, fuel)


'''
dynamic programming approach (iterative ver)

although it avoids recursion stacks but is damn slower
than the recursive ver due to too many access to array.
'''


class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        # dp[city][remaining fuel] = available count of routes
        dp = [[0] * (fuel+1) for _ in range(n)]
        
        '''
        base case: there's always at least 1 route
        for the finish city with any remaining fuel.
        '''
        for avail_fuel in range(fuel+1):
            dp[finish][avail_fuel] = 1
        
        '''
        iterate all combinations of city-to-city pairs
        from empty fuel to full fuel.
        '''
        for avail_fuel in range(fuel+1):
            # from city j to city i
            for i in range(n):
                for j in range(i, n):
                    if i == j:
                        # do not immediately revisit the current city
                        continue
                    if avail_fuel >= (distance := abs(locations[i] - locations[j])):
                        dp[i][avail_fuel] = (dp[i][avail_fuel] + dp[j][avail_fuel - distance]) % 1_000_000_007

        return dp[start][fuel]

