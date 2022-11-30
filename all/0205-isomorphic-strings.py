'''
leetcode 75 lv1 day 2

dict approach

initialize the conversion in the first occurance of every alphabet,
and find the violations.

note that each alphabet has unique and bidirectional mapping to another alphabet.
'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        bidirection conversion table: char of s <-> char of t
        '''
        table1, table2 = dict(), dict()
        
        for c1, c2 in zip(s, t):
            if table1.setdefault(c1, c2) != c2 or table2.setdefault(c2, c1) != c1:
                # violated conversion, s & t are not isomorphic.
                return False
        # s & t are isomorphic
        return True

