'''
2022/10/06 daily challenge

binary search approach

(if-else in while) runtime=757ms
(if-elif-else in while) runtime=1921ms
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

        the goal is to find not only the exact timestamp
        but also the nearest <=timestamp.

        we use the simplistic conditions to keep the runtime low
        and self._storage[key][right-1][1] is always the answer.
        '''
        series = self._storage[key]
        left = 0
        right = len(series)
        while left < right:
            mid = (left + right) // 2
            if series[mid][0] <= timestamp:
                left = mid + 1
            else:
                '''
                right is not a candidate but right-1 will be the answer in the end.
                '''
                right = mid
        
        # no need to check right==0 here as it's handled in the beginning.
        return series[right-1][1]

