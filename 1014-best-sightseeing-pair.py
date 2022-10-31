'''
dynamic programming approach

memorize current score and overall best score.
'''

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        curr = best = 0
        for spot in values:
            '''
            keep or reassign the best pair with (previous better spot + current spot.)
            '''
            best = max(best, curr + spot)
            '''
            keep the previous spot or replace it with current spot.
            minus the distance of 1 because we've one step forwarded.
            '''
            curr = max(curr, spot) - 1
        
        return best
