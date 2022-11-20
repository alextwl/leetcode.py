'''
2022/11/20 daily challenge

stack approach

always push current answer to the stack when entering into a parenthesis.
'''

class Solution:
    def calculate(self, s: str) -> int:
        ans = 0  # aggregated answer of the equation
        num = 0  # register of a number
        sign = 1  # register of last number's sign (only in [-1, 1])
        stack = list()  # for the parentheses
        
        for c in s:
            if c.isdigit():
                num = num * 10 + int(c)
            elif c in ['-', '+']:
                '''
                no matter whether it's an unary operation or not,
                add the registered number with **previous** registered sign to the answer,
                and update the sign register (for the next number) in the end.
                '''
                ans += sign * num
                # the num reg is cleared because it's added to the answer.
                num = 0
                # new sign for the next num
                sign = 1 if c == '+' else -1
            elif c == '(':
                # save current answer & next sign temporarily
                stack.append(ans)
                stack.append(sign)  # it's the sign of the following parenthesis' sum.
                # reset to default for the parenthesis.
                ans = 0
                sign = 1
            elif c == ')':
                '''
                the parenthesis is closed
                time to pop the outer registers, consider the equation reversely.
                
                sum(in the parenthesis) * the sign of the entire parenthesis + popped ans.
                '''
                ans += sign * num  # add last number in the parenthesis
                ans = ans * stack.pop()  # pop the sign of the entire parenthesis
                ans += stack.pop()  # add popped answer.
                
                # reset num reg. we don't reset the sign reg because next c will be an operator.
                num = 0
        
        ans += sign * num  # add last registered num
        
        return ans

