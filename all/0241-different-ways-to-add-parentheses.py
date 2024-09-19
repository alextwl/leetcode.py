'''
2024/09/19 daily challenge

recursion approach
'''


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        n = len(expression)

        if n == 0:
            return []
        
        if n == 1:
            # single digit
            return [int(expression)]
        
        if n == 2 and expression[0].isdigit():
            # 2-digit excluding negatives
            return [int(expression)]
        
        rets = []
        for i, c in enumerate(expression):
            if c.isdigit():
                continue
            left_rets = self.diffWaysToCompute(expression[:i])
            right_rets = self.diffWaysToCompute(expression[i+1:])
            
            for left in left_rets:
                for right in right_rets:
                    if c == "+":
                        rets.append(left + right)
                    elif c == '-':
                        rets.append(left - right)
                    else:
                        # c == "*"
                        rets.append(left * right)
        return rets

