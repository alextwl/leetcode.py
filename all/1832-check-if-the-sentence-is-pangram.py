'''
2022/10/17 daily challenge

use dict as set approach
'''

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        count = 0
        letters = dict()
        
        for c in sentence:
            if c not in letters:
                letters[c] = True
                count += 1
                if count == 26:
                    return True
        
        return False

