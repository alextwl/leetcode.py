'''
2023/05/31 daily challenge
'''

import collections


class UndergroundSystem:
    def __init__(self):
        self.checks = {}  # self.checks[id] = (startStation, beginTime)
        self.rideTimes = collections.defaultdict(int)  # self.rideTimes[(startStation, endStation)] = totalTime
        self.counts = collections.defaultdict(int)  # self.counts[(startStation, endStation)] = the count of passengers

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checks[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, beginTime = self.checks[id]
        stationPair = (startStation, stationName)
        self.rideTimes[stationPair] += t - beginTime
        self.counts[stationPair] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        stationPair = (startStation, endStation)
        return self.rideTimes[stationPair] / self.counts[stationPair]

