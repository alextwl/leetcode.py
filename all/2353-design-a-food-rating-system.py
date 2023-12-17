'''
2023/12/17 daily challenge

max heap approach
'''

import collections
import heapq


class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_cuisine = dict()
        self.food_rate = dict()
        self.heap_cuisine = collections.defaultdict(list)  # (-rating, food)
        for f, c, r in zip(foods, cuisines, ratings):
            self.food_cuisine[f] = c
            self.food_rate[f] = r
            # convert the max heap to min heap by reversing the rating
            heapq.heappush(self.heap_cuisine[c], (-r, f)) 

    def changeRating(self, food: str, newRating: int) -> None:
        c = self.food_cuisine[food]
        heapq.heappush(self.heap_cuisine[c], (-newRating, food))
        self.food_rate[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        h = self.heap_cuisine[cuisine]
        while(h):
            neg_r, f = h[0]
            # check the freshness of rating
            if self.food_rate[f] == -neg_r:
                return f
            
            # expired data, pop it.
            heapq.heappop(h)
        
        return None  # undefined behavior

