'''
2023/02/02 daily challenge
'''

import string


class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        mapping = {alien: human for alien, human in zip(order, string.ascii_lowercase)}

        if len(words) < 2:
            # no pairs are compared
            return True
        
        for i in range(1, len(words)):
            prev = words[i-1]
            curr = words[i]
            for x, y in zip(prev, curr):
                if mapping[x] < mapping[y]:
                    break
                elif mapping[x] > mapping[y]:
                    # the sequence is unsorted.
                    return False
                '''
                if mapping[x] == mapping[y]:
                    # continue comparing next character
                    pass
                '''
            else:
                if len(curr) < len(prev):
                    '''
                    if curr is a prefix of prev and shorter than prev,
                    it's curr < prev in lexicographical rules,
                    which is not sorted.
                    '''
                    return False
        # the sequence is sorted
        return True

