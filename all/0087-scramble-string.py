'''
2023/03/30 daily challenge

learnt from
https://leetcode.com/problems/scramble-string/solutions/3357546/python3-35ms-beats-99-38-recursion-with-memoization/
'''

class Solution:
    def __init__(self):
        self.m = dict()

    def isScramble(self, s1: str, s2: str) -> bool:
        # return previous result if (s1, s2) pair was already checked.
        if (s1, s2) in self.m:
            return self.m[(s1, s2)]

        # rule 1: if len(s1) == 1, stop
        # the string of length 1 is the minimun unit and cannot be scrambled,
        # so just check whether both strings are equivalent or not.
        if len(s1) == 1:
            return s1 == s2
        
        # if both sorted strings were not equivalent,
        # they are not possible to be a scrambled version of each other.
        if sorted(s1) != sorted(s2):
            return False
        
        # check all possible partitions recursively
        for i in range(len(s1)):
            # check if substring pairs were scrambled
            # in the swapped or non-swapped cases.
            if (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i])) or \
                (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:])):
                self.m[(s1, s2)] = True
                return True
        
        # no substrings are valid scrambled strings
        self.m[(s1, s2)] = False
        return False

