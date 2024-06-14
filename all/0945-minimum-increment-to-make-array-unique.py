'''
2024/06/14 daily challenge

counting sort + summation approach
'''

import collections


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        ctr = collections.Counter(nums)

        it = iter(sorted(ctr.keys()))
        prev_num = next(it)
        moves = 0
        seat_needed = ctr[prev_num] - 1

        for next_num in it:
            num_diff = next_num - prev_num
            
            if num_diff - seat_needed >= 1:
                # sufficient gap to fill all previous unassigned numbers
                moves += (seat_needed * (seat_needed + 1)) >> 1
                # fill 1 next_num into the current position and carry remainings to the next round.
                seat_needed = ctr[next_num] - 1
            else:
                # fill some previous numbers into the gap between previous and current position sequentially
                moves += (num_diff * (num_diff + 1)) >> 1
                seat_needed -= num_diff
                # move all unassigned numbers to current position
                moves += seat_needed * num_diff
                # insufficient space to fill next_num(s) in, carry it to the next round.
                seat_needed += ctr[next_num]
            
            prev_num = next_num
        
        # increment remaining largest numbers
        moves += (seat_needed * (seat_needed + 1)) >> 1

        return moves

