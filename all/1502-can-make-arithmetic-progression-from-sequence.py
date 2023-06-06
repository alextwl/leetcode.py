'''
2023/06/06 daily challenge
'''

class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        # sort it first
        arr.sort()

        # get diff between 1st & 2nd element
        it = iter(arr)
        one = next(it)
        two = prev = next(it)
        diff = two - one
        # compare each diff pair with the first pair.
        for curr in it:
            if curr - prev != diff:
                return False
            prev = curr

        return True

