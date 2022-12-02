'''
2022/12/02 daily challenge

Counter approach

intuition: if two words are close, it will meet the following conditions.
(1) two words have the same set of alphabets. (from Operation 1 & 2)
(2) the occurances of respective alphabets in two words are the same
    regardless of the sequence of alphabets. (from Operation 2)
'''

import collections


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            # words with different length are not close.
            return False
        
        # count the occurance of alphabets
        c1 = collections.Counter(word1)
        c2 = collections.Counter(word2)

        '''
        test whether two words have the same set of alphabets.
        the Operation 2 can only transform every occurrence of
        one **existing** character into another **existing** character,
        we cannot replace one character into another character
        which is not existed in either two words.
        '''
        if set(c1.keys()) != set(c2.keys()):
            return False
        
        '''
        check whether two words had the same occurance of alphabets.
        with the Operation 2 applied, we can just check the occurance regardless of alphabets.
        '''
        return sorted(c1.values()) == sorted(c2.values())

