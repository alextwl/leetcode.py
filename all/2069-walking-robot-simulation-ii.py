'''
2026/04/07 daily challenge

optimized simulation approach

learnt from official editorial:
https://leetcode.com/problems/walking-robot-simulation-ii/editorial/#approach-simulation

consider the robot starts from (0, 0) and move eastward,
when out of bounds, it turns 90 degrees counterclockwise and continues moving.
we can see the robot is **always** moving along with the boundary,
so that we can just prebuild the answers for all coordinates on the bounds.

simulation without any optimization will be TLE.
'''


DIR_NAME = ["East", "North", "West", "South"]


class Robot:
    def __init__(self, width: int, height: int):
        self.moved = False
        # a list of boundary coordinates start from (0, 0) anticlockwisely
        self.pos = []
        # a list of coordinate's current directions
        #
        # WWWWWWN
        # S     N
        # S     N
        # SEEEEEE
        #
        self.dirs = []
        # current position to self.pos
        self.idx = 0

        # build bounary coordinates & its directions to move
        for i in range(width):
            self.pos.append([i, 0])
            self.dirs.append(0)
        for i in range(1, height):
            self.pos.append([width - 1, i])
            self.dirs.append(1)
        for i in range(width - 2, -1, -1):
            self.pos.append([i, height - 1])
            self.dirs.append(2)
        for i in range(height - 2, 0, -1):
            self.pos.append([0, i])
            self.dirs.append(3)

        # corner case: when robot is at (0, 0)
        # it's facing East only when it's not moved yet,
        # otherwise it's facing South because it came from (0, 1).
        self.dirs[0] = 3

    def step(self, num: int) -> None:
        self.moved = True
        self.idx = (self.idx + num) % len(self.pos)

    def getPos(self) -> List[int]:
        return self.pos[self.idx]

    def getDir(self) -> str:
        return DIR_NAME[self.dirs[self.idx]] if self.moved else "East"

