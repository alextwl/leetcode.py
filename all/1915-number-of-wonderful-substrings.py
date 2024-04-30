'''
2024/04/30 daily challenge

prefix parity bitmask approach

learnt from official solution:
https://leetcode.com/problems/number-of-wonderful-substrings/solution/
'''


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        a = ord('a')
        # the frequency of parity bitmasks
        #
        # base case: empty prefix without any odd occurance of letters is also wonderful.
        freq = {0: 1}

        prefix_mask = 0
        ans = 0

        for ch in word:
            bit = ord(ch) - a

            # flip the char bit by XOR
            prefix_mask ^= (1 << bit)

            # if the mask was present, it means there are smaller prefixes
            # of substrings with **no** odd freq chars, so we count it.
            #
            # on the other hand, the mask is occured at least one time.
            # so the difference of mask is zero between the previous and current occurance.
            # that means we can append it to all substrings prior to it and count again.
            ans += freq.setdefault(prefix_mask, 0)
            freq[prefix_mask] += 1

            # iterate a to j as the exact only odd letter of substrings to count.
            #
            # this is to count the substrings with mask = (1 << odd_ch),
            # which is between odd_mask and prefix_mask.
            for odd_ch in range(0, 10):
                if (odd_mask := prefix_mask ^ (1 << odd_ch)) in freq:
                    ans += freq[odd_mask]

        return ans

