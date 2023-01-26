'''
2023/01/26 daily challenge

breadth first search approach

note the k stops do not include source and **destination**.
'''

import collections


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # build directed graph
        flightFrom = collections.defaultdict(dict)  # flightFrom[from][to] = price
        for fromCity, toCity, price in flights:
            flightFrom[fromCity][toCity] = price
        
        flied = 0  # the number of cities flied to
        visited = dict()  # visited[city] = lowest fare, do not revisit the city unless reduced fare, or it will be TLE.
        cheapest = float('inf')
        q = collections.deque([(src, 0)])  # (city, fare)
        while(q and flied <= k+1):
            nextCities = len(q)
            for _ in range(nextCities):
                city, currentFare = q.popleft()
                if city == dst:
                    if currentFare < cheapest:
                        cheapest = currentFare
                elif city not in visited or visited[city] > currentFare:
                    visited[city] = currentFare  # memorize lower fare arriving current city.
                    for nextCity, price in flightFrom[city].items():
                        q.append((nextCity, currentFare + price))
            flied += 1
        
        return cheapest if cheapest < float('inf') else -1

