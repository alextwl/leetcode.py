'''
2022/08/04 daily challenge

LCM/GCD approach, learnt from
https://leetcode.com/problems/mirror-reflection/solutions/2376355/python3-4-lines-geometry-w-explanation-t-m-92-81/

imagine the laser ray passes through multiple squares
and goes straight to a receptor without reflection.
we can see the laser line is also the diagonal of a rectangle.

try to fold the rectangle to a single square of width p,
observe the laser line, and we will see the line meets
a receptor as the requirement from the question,
so that we can find a way to calculate which receptor that ray will meet
by how we expands square to the previous rectangle.
'''

import math

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        # find height of the extended rectangle == LCM(p,q)
        height = p*q // math.gcd(p,q)

        if (height//q) & 1 == 0:
            '''
            if height//q is a multiple of 2,
            the ray will meet receptor 2 eventually
            because of the number of reflections.
            '''
            return 2

        '''
        also see the height is also a multiple of p
        and the parity of the multiple will decide
        which receptor (0 or 1) the ray will meet.
        '''
        return (height//p) & 1

