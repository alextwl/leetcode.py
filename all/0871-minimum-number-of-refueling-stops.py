'''
2022/08/20 daily challenge

learnt from official solution DP approach
'''
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # dp[t] = max miles we can get to using i refueling stops
        dp = [startFuel] + [0] * len(stations)
        
        for i, (location, capacity) in enumerate(stations):
            # determine if we cloud get to location i using t stops
            for t in range(i, -1, -1):
                if dp[t] >= location:
                    # t is reachable, try to refuel for max miles when reaching next stop
                    dp[t+1] = max(dp[t+1], dp[t] + capacity)
                    
        for i, distance in enumerate(dp):
            if distance >= target:
                # target using minimum i stops is reachable
                return i
        
        # target is unreachable
        return -1
