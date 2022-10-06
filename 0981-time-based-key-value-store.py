'''
2022/10/06 daily challenge

binary search approach
'''

from collections import defaultdict

class TimeMap:

    def __init__(self):
        '''
        self._storage[key] = [[timestamp, value], ...]
        '''
        self._storage = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self._storage[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self._storage:
            return ""
        
        if timestamp < self._storage[key][0][0]:
            '''
            self._storage[key][0][0] is always the oldest time-value
            when the constraint "All the timestamps of set are strictly increasing" applies,
            so if the timestamp provided was older than it, empty value is returned.
            '''
            return ""
        
        '''
        binary search timestamp
        '''
        series = self._storage[key]
        left = 0
        right = len(series)
        while left < right:
            mid = (left + right) // 2
            if series[mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid
        
        if right == 0:
            return ""
        else:
            return series[right-1][1]

