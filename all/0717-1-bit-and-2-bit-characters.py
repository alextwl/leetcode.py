'''
2025/11/18 daily challenge

if a bit started as 1, that must be a two-bit character which
consists of either 11 or 10, so try to decode it as the 2nd char,
and then the 1st.
'''


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        # shortcut
        if len(bits) > 1 and bits[-2] == 0:
            return True

        it = iter(bits)
        ans = False
        for v in it:
            if v:
                # 2nd: two-bit char
                next(it)  # the next bit is irrelevant
                ans = False
            else:
                # 1st: one-bit char
                ans = True
        return ans


'''
greedy method (parity check) approach

learnt from official editorial 2:
https://leetcode.com/problems/1-bit-and-2-bit-characters/editorial/#approach-2-greedy

iterate the bits reversely.
except the last bit, the loop stops at next 0's bit.

so we have several cases, if bits could be:

(1) [..., 0, 0], parity == 0.
(2) [..., 0, (even numbers of 1's bits), 0], parity == 0.
(3) [..., 0, (odd numbers of 1's bits), 0], parity == 1.

also notice the problem said the input ends with 0.
'''


class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        parity = bits.pop()
        while bits and bits.pop():
            parity ^= 1
        return parity == 0

