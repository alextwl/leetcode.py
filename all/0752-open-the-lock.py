'''
2024/04/22 daily challenge

shortest path approach (Dijkstra's algorithm)
'''

import collections
import heapq


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        if target == '0000':
            return 0

        def next_stops(lock_vals):
            next_stops_list = []
            for i in range(4):
                # clockwise
                if lock_vals[i] < '9':
                    next_lock = lock_vals[:i] + chr(ord(lock_vals[i]) + 1) + lock_vals[i+1:]
                else:
                    next_lock = lock_vals[:i] + '0' + lock_vals[i+1:]
                
                if next_lock not in deadends:
                    next_stops_list.append(next_lock)

                # counterclockwise
                if lock_vals[i] > '0':
                    next_lock = lock_vals[:i] + chr(ord(lock_vals[i]) - 1) + lock_vals[i+1:]
                else:
                    next_lock = lock_vals[:i] + '9' + lock_vals[i+1:]

                if next_lock not in deadends:
                    next_stops_list.append(next_lock)

            return next_stops_list

        # the minimum distance of each lock code
        min_lock_dist = collections.defaultdict(lambda: float('inf'))

        # min_heap = [(path_len, lock_vals)]
        h = [(0, '0000')]

        while h:
            path_len, current_lock = heapq.heappop(h)

            if path_len < min_lock_dist[current_lock]:
                min_lock_dist[current_lock] = path_len

                path_len += 1
                for child in next_stops(current_lock):
                    if child == target:
                        return path_len
                    heapq.heappush(h, (path_len, child))

        return -1


'''
level order traversal approach

since it's an unweighted graph, no need to use Dijkstra's.
'''

import collections


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if '0000' in deadends:
            return -1

        if target == '0000':
            return 0
        
        deadends = set(deadends)  # speedup

        def next_stops(lock_vals):
            next_stops_list = []
            for i in range(4):
                # clockwise
                if lock_vals[i] < '9':
                    next_lock = lock_vals[:i] + chr(ord(lock_vals[i]) + 1) + lock_vals[i+1:]
                else:
                    next_lock = lock_vals[:i] + '0' + lock_vals[i+1:]
                
                if next_lock not in deadends:
                    next_stops_list.append(next_lock)

                # counterclockwise
                if lock_vals[i] > '0':
                    next_lock = lock_vals[:i] + chr(ord(lock_vals[i]) - 1) + lock_vals[i+1:]
                else:
                    next_lock = lock_vals[:i] + '9' + lock_vals[i+1:]

                if next_lock not in deadends:
                    next_stops_list.append(next_lock)

            return next_stops_list

        visited = set()
        q = collections.deque(['0000'])

        path_len = 0
        while q:
            width = len(q)

            for _ in range(width):
                current_lock = q.popleft()
                if current_lock in visited:
                    continue
                visited.add(current_lock)
                if current_lock == target:
                    return path_len
                for child in next_stops(current_lock):
                    q.append(child)

            path_len += 1

        return -1

