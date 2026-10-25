'''
2026/10/24 daily challenge

prefix sums + count overlaps approach
'''


# 1-indexed prefix sums of days of previous months
PREV_DAYS = [0, 0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334, 365]


class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        alice_mm0, alice_dd0 = arriveAlice.split('-')
        alice_mm1, alice_dd1 = leaveAlice.split('-')
        bob_mm0, bob_dd0 = arriveBob.split('-')
        bob_mm1, bob_dd1 = leaveBob.split('-')

        # convert to day of a year
        alice_start = PREV_DAYS[int(alice_mm0)] + int(alice_dd0)
        alice_end = PREV_DAYS[int(alice_mm1)] + int(alice_dd1)
        bob_start = PREV_DAYS[int(bob_mm0)] + int(bob_dd0)
        bob_end = PREV_DAYS[int(bob_mm1)] + int(bob_dd1)

        if alice_end < bob_start or bob_end < alice_start:
            return 0

        start = max(alice_start, bob_start)
        end = min(alice_end, bob_end)
        return end - start + 1

