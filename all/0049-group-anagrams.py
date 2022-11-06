'''
2022/10/28 daily challenge

just-sort-every-word-and-hash-it approach
'''

import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        a dict of anagram groups with keys of sorted words.
        
        groups['sorted_word'] = ['anagram', ...]
        '''
        groups = collections.defaultdict(list)
        
        for s in strs:
            groups[''.join(sorted(s))].append(s)
        
        return groups.values()
