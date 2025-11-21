'''
2023/11/14 daily challenge
2025/11/21 daily challenge

exhaustive method approach (count all letters)
'''


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        all_letters = set(s)

        # iterate all possible combinations
        for lr_char in all_letters:
            # get the indices of leftmost & rightmost target letter in s.
            left, right = s.index(lr_char), s.rindex(lr_char)
            center_letters = set(s[left+1:right])

            ans += len(center_letters)

        return ans


'''
oneliner ver
'''


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        return sum(len(set(s[s.index(c)+1:s.rindex(c)])) for c in set(s))

