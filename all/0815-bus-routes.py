'''
leetcode 75 lv2 day 11

breadth first search approach

since the problem asked for **the least number** of buses taken,
using BFS to traverse routes & bus stops will be efficient.

note only we get on a bus of a route increases the answer (depth),
travel between bus stops in the same route does not add the depth.
'''

import collections


class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target:
            return 0

        # stop -> multiple routes that contains 
        g = collections.defaultdict(list)
        for route_no, route in enumerate(routes):
            for stop in route:
                g[stop].append((route_no, route))

        # hop on first bus from the source stop
        seen_stops = {source}
        seen_routes = {route_no for route_no, _ in g[source]}
        # iterate all bus routes that stop at source
        queue = collections.deque([(route_no, route, 1) for route_no, route in g[source]])  # (route_no, route, depth)
        while(queue):
            route_no, route, depth = queue.popleft()
            seen_routes.add(route_no)
            next_depth = depth+1
            # check stops in the route
            for stop in route:
                if stop == target:
                    # target arrived
                    return depth
                if stop in seen_stops:
                    # the stop was visited, no need to reiterate routes it belongs to.
                    continue
                seen_stops.add(stop)
                # add all routes the stop belongs to except we've travelled the route.
                for next_route_no, next_route in g[stop]:
                    if next_route_no in seen_routes:
                        continue
                    seen_routes.add(next_route_no)
                    queue.append((next_route_no, next_route, next_depth))

        # target is unreachable
        return -1

