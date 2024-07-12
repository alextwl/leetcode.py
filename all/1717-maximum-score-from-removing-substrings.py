'''
2024/07/12 daily challenge

stack approach

removing higher-scored pairs before lower-scored ones is always optimal.
'''


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def remove_sub(source, sub):
            stack = []
            for c in source:
                if c == sub[1] and stack and stack[-1] == sub[0]:
                    stack.pop()
                else:
                    stack.append(c)
            return ''.join(stack)

        if x > y:
            high_sub, low_sub = "ab", "ba"
        else:
            high_sub, low_sub = "ba", "ab"
            x, y = y, x

        # 1st pass: remove higher score pairs
        str_wo_high = remove_sub(s, high_sub)
        score = ((len(s) - len(str_wo_high)) // 2) * x

        # 2nd pass: remove lower score pairs
        str_stripped = remove_sub(str_wo_high, low_sub)
        score += ((len(str_wo_high) - len(str_stripped)) // 2) * y

        return score

