'''
2023/04/26 daily challenge

O(1) ver by observation

                                     v--- equal to remainder 0.
f(1)=1,  f(2)=2,  f(3)=3,  ..., f(9)=9,
f(10)=1, f(11)=2, f(12)=3, ..., f(18)=9,
f(19)=1, f(20)=2, f(21)=3, ..., f(27)=9,
...
f(91)=1, f(92)=2, f(93)=3, ..., f(99)=9,
f(100)=1, ...

the remainder of num divided by 9 is the ans.
'''

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            # special case: 0 is evenly divisible but there's only zero digit.
            return 0
        
        if (ans := num % 9) == 0:
            # special case: if the num is evenly divisible, return 9 for the requirement.
            return 9

        return ans

