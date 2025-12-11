'''
differential array approach
'''


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diffs = [0] * (n + 2)  # 1-indexed array
        for first, last, seats in bookings:
            diffs[first] += seats
            diffs[last + 1] -= seats
        # convert to 0-indexed array, dummy head/tail removed.
        diffs.pop(0)
        diffs.pop()

        ans = []
        reserved = 0
        for dv in diffs:
            reserved += dv
            ans.append(reserved)

        return ans

