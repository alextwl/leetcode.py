'''
2025/01/12 daily challenge

stack approach

validate locked parentheses first,
and then pair remained open brackets with unlocked chars.
'''


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) & 1:
            # odd length, impossible to validate
            return False
        
        opens = []
        unlocked = []

        for i, (c, locker) in enumerate(zip(s, locked)):
            if locker == '0':
                unlocked.append(i)
            elif c == '(':
                opens.append(i)
            else:
                # c == ')'
                if opens:
                    opens.pop()
                elif unlocked:
                    unlocked.pop()
                else:
                    return False

        # close remaining open brackets by unlocked slots
        while opens and unlocked and opens[-1] < unlocked[-1]:
            opens.pop()
            unlocked.pop()

        return False if opens else True

