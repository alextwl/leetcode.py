'''
2024/07/28 daily challenge

modified Dijkstra's algorithm with Top2 shortest lengthes tracking
'''


import functools
import heapq
import math


class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        @functools.lru_cache
        def get_next_time(currentTime):
            quo, rem = divmod(currentTime, change)
            if quo & 1:
                # the signal turned red, waits for the green light
                return currentTime - rem + change
            # the signal is already green, free to move.
            return currentTime

        # build graph
        g = {i: set() for i in range(1, n + 1)}
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)

        h = [(0, 1)]  # (time_elapsed, node)
        min_time1 = {i: math.inf for i in range(1, n + 1)}
        min_time2 = min_time1.copy()
        freq = {i: 0 for i in range(1, n + 1)}  # frequency of visiting a node

        while h:
            time_elapsed, node = heapq.heappop(h)
            
            freq[node] += 1
            if node == n and freq[node] == 2:
                return time_elapsed
            
            time_elapsed = get_next_time(time_elapsed) + time

            for child in g[node]:
                if freq[child] == 2:
                    continue
                if min_time1[child] > time_elapsed:
                    min_time2[child] = min_time1[child]
                    min_time1[child] = time_elapsed
                elif min_time2[child] > time_elapsed and min_time1[child] != time_elapsed:
                    min_time2[child] = time_elapsed
                else:
                    # no need to visit the child if the time elapsed is longer
                    # **or equivalent to the minimum.**
                    # (caution the definition of the second minimum time)
                    continue
                heapq.heappush(h, (time_elapsed, child))

        return -1  # undefined

# TODO: use BFS

