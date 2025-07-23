'''
2024/07/12 daily challenge
2025/07/23 daily challenge

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


'''
counter + greedy method approach

always form pairs with higher score, and then with lower score.
'''


class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        # assume a's score >= b's. if not, swap it.
        a, b = 'a', 'b'
        if x < y:
            a, b = 'b', 'a'
            x, y = y, x

        # counter of a & b seen (there's no non-ab char in the middle)
        a_cnt = b_cnt = 0
        ans = 0
        for c in s:
            if c == a:
                a_cnt += 1
            elif c == b:
                if a_cnt > 0:
                    # always form a pair of 'ab' greedily,
                    # use a previous 'a' and a current 'b' char here.
                    a_cnt -= 1
                    ans += x
                else:
                    b_cnt += 1
            else:
                # non-ab char encountered, try to form 'ba' pairs
                ans += min(a_cnt, b_cnt) * y
                a_cnt = b_cnt = 0  # reset by non-ab char

        # try to form 'ba' pairs again by remaining chars
        ans += min(a_cnt, b_cnt) * y
        return ans

