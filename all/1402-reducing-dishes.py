'''
2023/03/29 daily challenge

greedy approach
'''

class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        # sort it first.
        satisfaction.sort()

        if satisfaction[-1] <= 0:
            # no positive satisfaction collected.
            # people do not like the dishes, no dish is prepared.
            return 0
        
        coeff = 0  # coefficient
        diff = 0
        for t, s in enumerate(satisfaction, start=1):
            # calculate coefficient if all dishes were prepared.
            coeff += t * s
            diff += s
        
        # greedy method
        max_coeff = coeff
        for s in satisfaction:
            # remove dishes from the least satisfaction
            '''
            e.g. satisfaction = [-9,-8,-1,0,5],
                 initial coeff = -9*1 -8*2 -1*3 +0*4 +5*5 = -3
                 initial diff = sum([-9,-8,-1,0,5])

            To remove the first dish -9,
            the new coeff is initial coeff - diff  = -8*1 -1*2 +0*3 +5*4 = 10
            '''
            coeff -= diff
            '''
            the new diff is sum([-8,-1,0,5]) which also removed the first dish
            '''
            diff -= s
            if coeff > max_coeff:
                max_coeff = coeff
            else:
                # the maximum sum of like-time coefficient found,
                # no more dishes can be removed.
                return max_coeff
        
        return max_coeff

