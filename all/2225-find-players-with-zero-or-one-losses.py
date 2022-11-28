'''
2022/11/28 daily challenge

count the matches with one array with multiple status indicating
whether player has played or not and their losses.

time=O(3n), space=O(n)
Runtime: 7960 ms, faster than 5.06% of Python3 online submissions
'''

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        '''
        losses[i] =
        -1: i-th player does not yet have a match.
         0: i-th player does not lose any matches.
         1: i-th player loses exactly one match.
        >1: i-th player loses multiple matches.
        '''
        losses = [-1] * 100001
        
        for winner, loser in matches:
            if losses[winner] == -1:
                # flag the first match
                losses[winner] = 0
            losses[loser] = 1 if losses[loser] < 1 else 2  # 2 == multiple losses, no need to count further
        
        allwin = [player for player, loss in enumerate(losses) if loss == 0]  # haven't lost any matches and played at least one match.
        oneloss = [player for player, loss in enumerate(losses) if loss == 1]  # have lost exactly one match.
        
        return [allwin, oneloss]


'''
hashmap + builtin sorting approach

Runtime: 1902 ms, faster than 94.37%
apparantly python's dict access is much faster than list...
'''

import collections

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        # count losers first
        losses = collections.Counter(loser for _, loser in matches)
        # and count all winners (== won any matches and no loss)
        allwin = [winner for winner in sorted(set(winner for winner, _ in matches) - set(losses))]
        # count losers with exact one loss
        oneloss = [loser for loser, loss in losses.items() if loss == 1]
        oneloss.sort()
        
        return [allwin, oneloss]

