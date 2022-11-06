'''
2022/09/12 daily challenge
learnt from official solution

greedy method

the idea is to play tokens face up as more as possible first,
and then play tokens face down moderately
if there's any chance to earn more score by more power.
'''

import collections

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        deque = collections.deque(tokens)
        
        max_score = 0
        current_score = 0
        
        '''
        conditions:
        1. each token may be played at most once. (use deque to guratantee)
        2. token face up if power >= token
        3. token face down if score >= 1
        '''
        while deque and \
                (power >= deque[0] or 
                 current_score):
            # play tokens face up as more as possible
            # from the smallest power of token (popleft)
            while deque and power >= deque[0]:
                power -= deque.popleft()
                current_score += 1
            
            max_score = max(max_score, current_score)
            
            # time to play a token face down
            # from the biggest power of token (pop right)
            # only if score is at least 1
            # in order to gain more power for further higher score in the next round of loop.
            if deque and current_score:
                power += deque.pop()
                current_score -= 1
        
        return max_score
