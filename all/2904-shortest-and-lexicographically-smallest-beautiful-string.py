'''
2026/08/26 daily challenge

sliding window approach
'''


class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ones = 0
        i = 0
        sub = '1' * 101  # init with an out-of-range lexicographically largest

        for j, c in enumerate(s):
            if c == '1':
                ones += 1
            # shrink the window greedily
            while i <= j and (ones > k or s[i] == '0'):
                if s[i] == '1':
                    ones -= 1
                i += 1
            if ones == k:
                sublen = (j - i) + 1
                curr_sub = s[i:j+1]
                # shorter one always prevails,
                # and then lexicographically smaller one if same length.
                if sublen < len(sub) or (sublen == len(sub) and curr_sub < sub):
                    sub = curr_sub

        return "" if len(sub) == 101 else sub

