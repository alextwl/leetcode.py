'''
2023/06/09 daily challenge
2026/01/31 daily challenge

binary search approach
'''

import string


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        if target == 'z':
            return letters[0]
        
        '''
        create a character-to-lexicographical-index dict
        '''
        lex = {c: i for i, c in enumerate(string.ascii_lowercase)}
        tlex = lex[target]
        
        left, right = 0, len(letters)-1
        while(left <= right):
            mid = left + (right-left)//2
            mlex = lex[letters[mid]]
            '''
            if target existed, we need to find its next letter.
            '''
            if mlex <= tlex:
                left = mid + 1
            else:
                right = mid - 1
        
        if left >= len(letters):
            return letters[0]

        return letters[left]


'''
oneliner ver
'''


import bisect


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect.bisect_right(letters, target) % len(letters)]

