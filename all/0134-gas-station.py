'''
2023/01/07 daily challenge

greedy approach

always restart from the station next to the last visited station
because we will stop at the last visited station if we started
from any previously visited stations (0 <= i <= last.)
'''


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # just find the start station first.
        start = 0
        while(start < len(gas)):
            if cost[start] > gas[start]:
                # not enough gas to travel to the next station
                start += 1
                continue
            # try to travel around the circuit
            tank = gas[start] - cost[start]
            arrival = start + 1
            if arrival >= len(gas): arrival = 0
            while(arrival != start):
                tank += gas[arrival] - cost[arrival]
                if tank < 0:
                    # not enough gas to travel to the next station
                    break
                # go to the next station.
                arrival += 1
                if arrival >= len(gas): arrival = 0
            else:
                # the car has travelled around the circuit.
                return start
            
            # try to start from the next station.
            if arrival < start:
                '''
                it's not possible to start from the previous starting stations
                because the gas will be never enough when we visit current station again.
                '''
                return -1
            start = arrival + 1

        # the starting gas station is not found.
        return -1

