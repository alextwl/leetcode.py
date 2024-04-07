'''
2024/04/07 daily challenge

stack approach

learnt from official solution 3
https://leetcode.com/problems/valid-parenthesis-string/solution/

memorize the positions of open parentheses and wildcard char by 2 stacks
and try to balance it.
'''


class Solution:
    def checkValidString(self, s: str) -> bool:
        # the stack of positions of unbalanced open parentheses and unused wildcard char
        stack_open = []
        stack_wildcards = []
        
        for i, c in enumerate(s):
            if c == '(':
                stack_open.append(i)
            elif c == '*':
                stack_wildcards.append(i)
            else:
                # c == ')'
                if stack_open:
                    # make a pair of parentheses
                    stack_open.pop()
                elif stack_wildcards:
                    # or use a wildcard char as a left bracket
                    stack_wildcards.pop()
                else:
                    # impossible to balance the closing parentheses
                    # because of insufficient open parentheses or wildcards
                    return False
        
        while stack_open and stack_wildcards:
            if stack_open.pop() > stack_wildcards.pop():
                # an open parentheses cannot be balanced by
                # a wildcard char in the left side.
                return False

        # all open parentheses should be balanced and the stack is empty
        return not(stack_open)

