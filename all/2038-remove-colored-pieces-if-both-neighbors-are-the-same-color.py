'''
2023/10/02 daily challenge

counter approach

(1) for any group of same color consecutive pieces,
the player can remove n - 2 pieces.

(2) there's no chance to merge two groups because of the limitation of rule.

e.g. BBBABBB for example, we cannot merge left BBB & right BBB
because cannot remove center A.

so the sequence of removal operations is irrelevant,
we can simply count it and doesn't need to run dynamic programming like stone game.

(3) while the problem does not mention explicitly, Alice always plays first.
'''


class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if len(colors) < 3:
            # Bob always wins if Alice couldn't start the game.
            return False

        # the number of removal operations by each player
        removals = {'A': 0, 'B': 0}
        
        it = iter(colors)
        prev2 = next(it)
        prev1 = next(it)
        
        for curr in it:
            if prev2 == prev1 == curr:
                removals[curr] += 1
            prev2, prev1 = prev1, curr
        
        return (removals['A'] - removals['B']) > 0

