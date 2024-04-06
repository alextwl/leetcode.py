'''
2024/04/06 daily challenge

two-pass stack approach

1st pass: remove extra closing parentheses if
          earlier open parentheses was not sufficient to make pairs.

2nd pass: remove extra open parentheses reversely if
          there's no more closing parentheses after that to make pairs.
'''


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        open_count = 0
        stack = []

        # scan the input string from left to right
        for c in s:
            if c == '(':
                open_count += 1
            elif c == ')':
                if not open_count:
                    # insufficient open parentheses,
                    # ignore this closing char ')'.
                    continue
                # close a pair of parentheses
                open_count -= 1

            stack.append(c)

        # scan the stack from right to left
        # to find extra open parenthesis char '('
        rev_ans = []
        while stack:
            c = stack.pop()
            if open_count and c == '(':
                # delete the extra open char because
                # there's no more sufficient closing char to make a pair with it.
                open_count -= 1
            else:
                rev_ans.append(c)

        return ''.join(reversed(rev_ans))

