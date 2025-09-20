'''
2025/09/20 daily challenge

hashmap + binary search approach

hash packet headers and queue timestamps grouped by destinations.
'''


import bisect
import collections


class Router:
    def __init__(self, memoryLimit: int):
        self.size = memoryLimit
        self.tuples = set()
        self.q = collections.deque()
        self.dst_q = collections.defaultdict(collections.deque)

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        pkt = (source, destination, timestamp)
        if pkt in self.tuples:
            return False
        if len(self.q) >= self.size:
            old = self.q.popleft()
            self.tuples.remove(old)
            self.dst_q[old[1]].popleft()
        self.q.append(pkt)
        self.tuples.add(pkt)
        self.dst_q[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if self.q:
            pkt = self.q.popleft()
            self.tuples.remove(pkt)
            self.dst_q[pkt[1]].popleft()
            return list(pkt)
        return []

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        # binary search the range in the queue of same destination packets.
        return bisect.bisect_right(self.dst_q[destination], endTime) - bisect.bisect_left(self.dst_q[destination], startTime)

