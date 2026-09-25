'''
2026/09/25 daily challenge

stack approach
'''


class Solution:
    def braceExpansionII(self, expression: str) -> list[str]:
        stack = []
        ops = []

        def evaluate():
            left = len(stack) - 2
            right = len(stack) - 1
            if ops[-1] == ",":
                stack[left] |= stack[right]
            else:
                tmp = set()
                for ll in stack[left]:
                    for rr in stack[right]:
                        tmp.add(ll + rr)
                stack[left] = tmp
            ops.pop()
            stack.pop()

        prev = ""
        for i, c in enumerate(expression):
            if c == '{':
                if i > 0 and (prev == '}' or prev.isalpha()):
                    # cartesian product pending
                    ops.append('*')
                ops.append('{')
            elif c == '}':
                while ops and ops[-1] != '{':
                    evaluate()
                ops.pop()
            elif c == ',':
                while ops and ops[-1] == '*':
                    evaluate()
                ops.append(',')
            else:
                if i > 0 and (prev == '}' or prev.isalpha()):
                    ops.append('*')
                stack.append({c})  # convert to a singleton set
            prev = c

        while ops:
            evaluate()

        return sorted(stack[-1])

