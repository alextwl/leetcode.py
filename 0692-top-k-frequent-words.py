'''
2022/10/19 daily challenge

pythonic approach

use heapq.nsmallest with negative priority (count) to get top-K frequent words.
https://docs.python.org/3/library/heapq.html#heapq.nsmallest
'''

import collections, heapq

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        wdict = collections.defaultdict(int)
        
        # count each word in words.
        for w in words:
            wdict[w] += 1
        
        '''
        while the negative count (-wdict[w]) is the primary key,
        the word (w) itself should be the secondary key because
        the problem asks for sorting them with the *same* frequency
        by their lexicographical order.

        don't use heapq.nlargest here because it results in
        reversed lexicographical order for the same freq words.
        '''
        return heapq.nsmallest(k, wdict, key=lambda w: (-wdict[w], w))
