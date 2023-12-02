'''
2023/12/02 daily challenge

counter approach
'''

import collections


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cpool = collections.Counter(chars)
        
        ans = 0
        for w in words:
            if all(cpool[k] >= v for k, v in collections.Counter(w).items()):
                ans += len(w)

        return ans

