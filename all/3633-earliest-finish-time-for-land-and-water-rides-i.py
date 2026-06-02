'''
2026/06/02 daily challenge

brute force approach
'''


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        min_time = float('inf')
        for st0, dur0 in zip(landStartTime, landDuration):
            land_first = st0 + dur0
            for st1, dur1 in zip(waterStartTime, waterDuration):
                water_first = max(st1 + dur1, st0) + dur0
                min_time = min(min_time, max(land_first, st1) + dur1, water_first)
        return min_time

