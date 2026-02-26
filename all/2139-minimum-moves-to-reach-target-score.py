'''
greedy method approach

divide the target as many as possible
until the quota of maxDoubles exhausted.

all remainders also count same number of moves.
'''


class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        ans = 0

        while target > 1 and maxDoubles:
            if target & 1:
                # RSB=1, reverse the increment
                target -= 1
            else:
                # RSB=0, reverse the double
                target >>= 1
                maxDoubles -= 1
            ans += 1

        # if target > 1, count the difference as moves of increment
        return ans + (target - 1)

