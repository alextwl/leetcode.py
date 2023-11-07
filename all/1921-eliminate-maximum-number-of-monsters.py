'''
2023/11/07 daily challenge

sort the monsters by the order of arriving the city
'''


class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arrive_time = [d/s for d, s in zip(dist, speed)]
        arrive_time.sort()
        
        for i, arrival in enumerate(arrive_time):
            if i >= arrival:
                # impossible to eliminate this monster
                return i

        return i+1

