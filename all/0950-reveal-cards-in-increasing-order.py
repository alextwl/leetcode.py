'''
2024/04/10 daily challenge

reverse simulation approach
'''

import collections


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        # new deck in reversed order, [bottom ... top]
        rev = collections.deque([deck.pop()])
        
        while(deck):
            card = deck.pop()
            
            # move the bottom of card to top
            bottom = rev.popleft()
            rev.append(bottom)
            
            # place the card back to the top
            rev.append(card)
        
        rev.reverse()
        return list(rev)

