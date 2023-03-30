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


'''
iterative dynamic programming ver

learnt from
https://leetcode.com/problems/scramble-string/solutions/3357435/python-java-c-simple-solution-easy-to-understand/
'''

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # both strings are the same and always a scrambled version of each other.
        if s1 == s2:
            return True

        # if both sorted strings were not equivalent,
        # they are not possible to be a scrambled version of each other.
        if sorted(s1) != sorted(s2):
            return False
        
        n = len(s1)
        # 3D dp space: dp[i][j][length]
        # i: substring starting from s1[i]
        # j: substring starting from s2[j]
        # length: the length of the substring
        dp = [[[False] * (n+1) for _ in range(n)] for _ in range(n)]

        # initial check for length-1 substrings (Rule 1)
        for i, c1 in enumerate(s1):
            for j, c2 in enumerate(s2):
                dp[i][j][1] = (c1 == c2)
        
        # check for length>=2 substrings
        for length in range(2, n+1):
            for i in range(n-length+1):
                for j in range(n-length+1):
                    # substrings will be eventually splitted into minimum length-1 strings
                    # so we need to refer to dp[*][*][1] values.
                    for k in range(1, length):
                        if (dp[i][j][k] and dp[i+k][j+k][length-k]) or \
                            (dp[i][j+length-k][k] and dp[i+k][j][length-k]):
                            dp[i][j][length] = True
                            break

        # the result of both full s1 & s2 with full length is the answer.
        return dp[0][0][n]

