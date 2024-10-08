'''
2024/10/08 daily challenge

math approach

skip balanced pairs and count unbalanced right brackets.
'''


class Solution:
    def minSwaps(self, s: str) -> int:
        left_bracket = 0
        right_unbalanced = 0
        
        for c in s:
            if c == '[':
                left_bracket += 1
            else:
                if left_bracket:
                    left_bracket -= 1
                else:
                    right_unbalanced += 1
        
        # each swap balances two new pairs,
        # so the minimum swaps == ceil(half number of unbalanced right brackets)
        return (right_unbalanced + 1) >> 1

