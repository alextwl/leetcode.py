'''
2022/11/03 daily challenge

hash + count approach, learnt from official solution 1.

consider various cases:

(1) for word which is already a palindrome may consist of a longer palindrome.
  a. there may be only one central palindrome word. (e.g. cc in [ab, cc, ba])
  b. we can have multiple palindrome pairs of even counts. (e.g. [aa, bb, bb, aa])
(2) for word which is non-palindrome, find its reversed word. (e.g. for 'ab', find 'ba'.)
'''

import collections


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        count = collections.Counter(words)  # count the occurance of each word.
        centralWord = False  # flag indicates whether central palindrome exists or not.
        ansWords = 0  # the count of words which are concatenated as a longest palindrome.
        
        for key, num in count.items():
            # case 1. check if it's palindrome.
            if key[0] == key[1]:
                if num % 2:
                    '''
                    case 1a. odd count of palindrome found. there will be a central palindrome.
                    count its even parts first.
                    '''
                    ansWords += num - 1  # subtract odd
                    # there may be only one central palindrome word, set flag first.
                    centralWord = True
                else:
                    '''
                    cast 1b. even count of palindrome found.
                    all of the words can be concatenated with the longest palindrome.
                    '''
                    ansWords += num
            elif key[0] < key[1]:
                '''
                case 2. find a pair of non-palindrome words.
                we only check a pair once here.
                (for ['ab', 'ba'], 'a' < 'b' == True, 'b' < 'a' == False.)
                '''
                ansWords += min(num, count[key[1] + key[0]]) * 2  # count pairs by min() and then count words of pairs.
        if centralWord:
            # we can have only one central palindrome.
            ansWords += 1
        return ansWords * 2  # return the length of longest palindrome.

