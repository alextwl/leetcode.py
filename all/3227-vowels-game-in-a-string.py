'''
2025/09/12 daily challenge

greedy method approach (game theory)

if there's any vowel in the string, Alice always wins.

(1) if there's odd number of vowels, Alice can remove entire string to win.

(2) if there's non-zero even number of vowels, Alice can remove a substring
    as long as possible, leave one vowel (and several consonant if available).
    Bob will lose if there's no more consonant in 2nd round, or lose in
    4th round with empty string because Alice shall remove the entire string
    in 3rd round.

(3) Alice loses only if failed starting first round.
'''


class Solution:
    def doesAliceWin(self, s: str) -> bool:
        for c in s:
            if c in "aeiou":
                return True
        return False

