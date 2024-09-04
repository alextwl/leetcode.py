'''
2024/09/04 daily challenge

binary search approach
'''


import collections
import bisect


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        curr_dir = 0  # init toward to DOWN

        ob_rows = collections.defaultdict(list)
        ob_cols = collections.defaultdict(list)
        
        for x, y in obstacles:
            ob_rows[x].append(y)
            ob_cols[y].append(x)
        
        for row in ob_rows.values():
            row.sort()
        for col in ob_cols.values():
            col.sort()

        x, y = 0, 0
        max_dist = 0
        for cmd in commands:
            if cmd == -2:
                # turn left 90 degrees (clockwise)
                curr_dir = (curr_dir + 1) % 4
            elif cmd == -1:
                # turn right 90 degrees (anticlockwise)
                curr_dir = (curr_dir - 1) % 4
            else:
                # note there's a corner case when we start from (0, 0) with an obstacle,
                # we need to find the nearest obstacle by different variants of bisect.
                #print("from (%d, %d) " % (x, y), end='')
                if curr_dir == 0:
                    # go downward
                    #print("DOWN, ", end='')
                    i = bisect.bisect_right(ob_rows[x], y)
                    y += cmd
                    if ob_rows[x] and i < len(ob_rows[x]):
                        y = min(y, ob_rows[x][i] - 1)
                elif curr_dir == 1:
                    #print("LEFT, ", end='')
                    # go leftward
                    i = bisect.bisect_left(ob_cols[y], x)
                    x -= cmd
                    if ob_cols[y] and i > 0:
                        x = max(x, ob_cols[y][i-1] + 1)
                elif curr_dir == 2:
                    # go upward
                    #print("UP, ", end='')
                    i = bisect.bisect_left(ob_rows[x], y)
                    y -= cmd
                    if ob_rows[x] and i > 0:
                        y = max(y, ob_rows[x][i-1] + 1)
                else:
                    # go rightward
                    #print("RIGHT, ", end='')
                    i = bisect.bisect_right(ob_cols[y], x)
                    x += cmd
                    if ob_cols[y] and i < len(ob_cols[y]):
                        x = min(x, ob_cols[y][i] - 1)
                
                #print("to (%d, %d)" % (x, y))
                max_dist = max(max_dist, (x**2) + (y**2))

        return max_dist

