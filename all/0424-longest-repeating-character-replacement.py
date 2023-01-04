'''
leetcode 75 lv1 day 12

sliding window approach

maintain the letters' counters while moving sliding window
and shrink the window to the possible maximum length.
'''

import string


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {c: 0 for c in string.ascii_uppercase}
        maxcount = 0  # the maximum amount of a letter in s.
        left = 0
        longest = 0  # the answer

        for right, c in enumerate(s):
            counts[c] += 1
            '''
            get the current amount of the most frequent letter
            as the longest repeating character.
            '''
            maxcount = max(counts.values())

            '''
            shrink the window size from s[left..right] to maxcount + k.
            '''
            while((right-left+1) - maxcount) > k:
                counts[s[left]] -= 1
                left += 1
            
            longest = max(longest, right-left+1)
        
        return longest

