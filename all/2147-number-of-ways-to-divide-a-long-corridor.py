'''
2023/11/28 daily challenge

combination approach

count plants as a separator and calculate the number of combinations.
'''


class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seat_count = corridor.count('S')
        if not seat_count or seat_count & 1:
            # no seat or odd seats discovered, no way to divide it.
            return 0
        
        # base case: at least 1 way to divide
        ans = 1

        it = iter(corridor)

        seat = 0
        while(True):
            # stage 1: finding 2 seats, skipping any plants
            for c in it:
                if c == 'S':
                    seat += 1
                if seat >= 2:
                    break
            else:
                # end of corridor
                break

            # stage 2: count plants until another seat reached
            plant = 0
            for c in it:
                if c == 'P':
                    plant += 1
                else:
                    break
            else:
                # end of corridor, no need to divide.
                break

            # there are (plant+1) ways to divide the current corridor
            if plant:
                ans = (ans * (plant + 1)) % 1_000_000_007

            # reset the seat count, the last position must be a seat
            seat = 1

        return ans

