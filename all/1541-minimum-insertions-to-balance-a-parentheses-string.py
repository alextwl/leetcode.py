'''
2026/10/09 daily challenge

greedy method approach

try to make all pairs of parentheses balanced linearly.
'''


class Solution:
    def minInsertions(self, s: str) -> int:
        opened = 0
        closed = 0
        insert = 0
        for c in s:
            if c == '(':
                opened += 1
                if closed & 1:
                    insert += 1
                    closed += 1
                # cannot allow all unpaired closing brackets preceeding an opening one.
                while closed:
                    opened -= 1
                    closed -= 2
                    if opened == 0:
                        insert += 1
            else:
                closed += 1
                # try to pair two closing brackets with one opening bracket.
                if opened == 0:
                    opened += 1
                    insert += 1
                if closed >= 2:
                    opened -= 1
                    closed -= 2
        # count of remaining closing brackets to be paired must be even.
        if closed & 1:
            insert += 1
            closed += 1

        opened *= 2
        if opened > closed:
            insert += opened - closed
        elif opened < closed:
            insert += (closed - opened) // 2
        return insert

