'''
2024/10/20 daily challenge

stack approach
'''


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        stack = [['|',[]]]  # init with a dummy header

        for c in expression:
            if c == ',':
                continue
            elif c == 't':
                stack[-1][1].append(True)
            elif c == 'f':
                stack[-1][1].append(False)
            elif c == ')':
                # pop stack and evaluate it
                op, expr_list = stack.pop()
                if op == '&':
                    stack[-1][1].append(all(expr_list))
                elif op == '|':
                    stack[-1][1].append(any(expr_list))
                else:  # logical not
                    stack[-1][1].append(not expr_list[0])
            elif c == '(':
                continue
            else:  # new inner expressions !,&,|
                stack.append([c, []])

        return stack[0][1][0]

