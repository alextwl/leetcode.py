'''
2026/06/03 daily challenge

linear enumeration + classified earlist end time approach

same to problem 3363 with larger input.
'''


class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        # get completed time of the earlist rides
        min_end_land = min(st + dur for st, dur in zip(landStartTime, landDuration))
        min_end_water = min(st + dur for st, dur in zip(waterStartTime, waterDuration))
        min_ans = float('inf')

        # land ride first
        for st, dur in zip(waterStartTime, waterDuration):
            min_ans = min(min_ans, max(st, min_end_land) + dur)

        # water ride first
        for st, dur in zip(landStartTime, landDuration):
            min_ans = min(min_ans, max(st, min_end_water) + dur)

        return min_ans

