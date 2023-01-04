'''
leetcode 75 lv1 day 13

counter approach
'''

import collections


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        secret_counts = collections.Counter(secret)
        guess_counts = collections.Counter(guess)
        bulls = 0
        cows = 0

        # count bulls
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
        
        # count cows (including bulls)
        for hchar in range(ord('0'), ord('9')+1):
            cows += min(secret_counts[chr(hchar)],
                        guess_counts[chr(hchar)])
        cows -= bulls  # remove bulls

        return "%dA%dB" % (bulls, cows)

