'''
2024/12/27 daily challenge

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

            hint: from the equation of the score

            values[i] + values[j] + i - j

            the diff of indices (i - j) is included in curr.
            since j was growing with iteration, we always subtract 1
            from curr in each loop.
            '''
            curr = max(curr, spot) - 1
        
        return best
