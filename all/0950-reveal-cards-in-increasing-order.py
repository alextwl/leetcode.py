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


'''
fill the gap approach

intuition: observe the sequence of deck.

(1)
deck = [2,3,5,7,11,13,17]
new = [0,0,0,0,0,0,0]

(2)
new = [2,0,3,0,5,0,7]

(3)
new = [2,0,3,11,5,0,7]

(4)
new = [2,13,3,11,5,0,7]

(5)
new = [2,13,3,11,5,17,7]
'''


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        
        n = len(deck)
        ret = [0] * n  # new deck
        
        i = 0  # the current index of deck
        j = 0  # the current index of new deck to be returned
        skip = False  # the flag to skip or not to skip the next gap

        while(i < n):
            if not ret[j]:
                if not skip:
                    # fill the gap with the current card
                    ret[j] = deck[i]
                    i += 1
                # skip or not to skip the next gap
                skip = not skip
            # if the new deck pointer reached the end,
            # search the gap back and forth
            j = (j + 1) % n

        return ret

