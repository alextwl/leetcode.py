'''
2024/05/29 daily challenge

bitwise simulation approach
'''


class Solution:
    def numSteps(self, s: str) -> int:
        # convert to number array
        bits = [int(c) for c in s]
        
        steps = 0

        while len(bits) > 1:
            # even: do shifting
            while bits[-1] == 0:
                bits.pop()
                steps += 1
            
            # odd: add 1 to it
            if len(bits) > 1:
                steps += 1
                for i in range(len(bits) - 1, -1, -1):
                    if bits[i] == 0:
                        bits[i] = 1
                        break
                    else:
                        bits[i] = 0
                else:
                    bits.insert(0, 1)

        return steps

