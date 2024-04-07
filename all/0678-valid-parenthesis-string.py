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


'''
bottom-up dynamic programming approach
'''


class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        # dp[i][j] = the boolean of validity for the substring s[i:]
        #            with j open parentheses **unbalanced**
        dp = [[False] * (n+1) for _ in range(n+1)]
        
        # base case: empty string with zero open parentheses is valid
        dp[-1][0] = True
        
        for i in range(n-1, -1, -1):
            for j in range(n):
                # try to insert s[i] to the beginning of s[i+1:] substring
                # and calculate its validity
                is_valid = False

                if s[i] == '*':
                    # use '*' as '(', so there're one more open parentheses unbalanced
                    is_valid |= dp[i+1][j+1]
                    # use '*' as ')', balance a pair of parentheses
                    if j > 0:
                        is_valid |= dp[i+1][j-1]
                    # use '*' as an empty char
                    is_valid |= dp[i+1][j]
                elif s[i] == '(':
                    is_valid |= dp[i+1][j+1]
                elif j > 0:
                    # s[i] == ')' and there's sufficient open parentheses to be balanced
                    is_valid |= dp[i+1][j-1]
                
                dp[i][j] = is_valid

        # return the validity of full s[0:] with zero open parentheses (all balanced)
        return dp[0][0]


'''
two pointer approach

the intuition is similar to the two-pass stack approach of problem 1249.

count open parentheses & wildcards from left,
count closing parentheses & wildcard from right,
and validate if it's impossible to balance.
'''


class Solution:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        open_count = close_count = 0

        for i, j in zip(range(n), range(n-1, -1, -1)):
            if s[i] == ')':
                open_count -= 1
            else:
                # s[i] == '(' or '*'
                open_count += 1

            if s[j] == '(':
                close_count -= 1
            else:
                # s[j] == ')' or '*'
                close_count += 1

            if open_count < 0 or close_count < 0:
                # not enough open/closing parentheses
                return False

        return True

