'''
2026/05/12 daily challenge

sorting + greedy method approach
'''


class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # sort by unused energy after consumed
        tasks.sort(key=lambda x: x[1] - x[0])
        fuel = 0
        for spend, req in tasks:
            fuel = max(fuel + spend, req)
        return fuel

