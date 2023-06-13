'''
2023/06/11 daily challenge

binary search approach

learnt from official solution
https://leetcode.com/problems/snapshot-array/solution/

the main idea of the official solution is memorizing
the current version with each call setting any data,
and then binary searching the history.

do not make any copies or do any checks when running snap()
or the submission will be TLE.
'''

import bisect


class SnapshotArray:

    def __init__(self, length: int):
        self.sid = 0  # it's the interval version of current snapshot
        '''
        self.history[index] = [(version, val), (version, val), ...]
        all index are initialized with version=0 and val=0.
        '''
        self.history = [[(0,0)] for _ in range(length)]

    def set(self, index: int, val: int) -> None:
        self.history[index].append((self.sid, val))

    def snap(self) -> int:
        self.sid += 1
        return self.sid - 1  # minus 1 upon the question asks

    def get(self, index: int, snap_id: int) -> int:
        target = bisect.bisect_right(self.history[index], (snap_id, 1_000_000_000))
        return self.history[index][target - 1][1]

