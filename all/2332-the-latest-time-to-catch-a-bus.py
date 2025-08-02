'''
sorting + greedy method approach
'''


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()
        n = len(passengers)

        i = 0  # the index of a passenger to line up
        for t in buses:
            seats = capacity
            while i < n and passengers[i] <= t and seats:
                i += 1
                seats -= 1

        if seats:
            # the latest bus still has empty seat(s)
            latest = t
        else:
            # we should arrive before some passengers
            latest = passengers[i - 1]

        # caveat: the problem has constraint that "You cannot arrive at the same time as another passenger",
        # the arrival time of ours and others must be staggered.
        pset = set(passengers)
        while latest in pset:
            latest -= 1

        return latest

