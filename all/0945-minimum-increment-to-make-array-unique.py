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


'''
space=O(max(nums)) ver

Runtime: 529 ms, faster than 99.77% of Python3 online submissions
'''


class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        m = max(nums)
        
        # build the frequencies of numbers
        ctr = [0] * (m + 1)
        for v in nums:
            ctr[v] += 1
        
        moves = 0
        carry = 0

        # check each frequency of number and do increment
        for freq in ctr:
            # move all unassigned numbers to the current position
            moves += carry
            # proceed incoming numbers
            carry += freq
            # assign one number to the current position
            if carry:
                carry -= 1

        # assign remaining numbers to the positions after max(nums)
        if carry:
            moves += (carry * (carry + 1)) >> 1

        return moves

