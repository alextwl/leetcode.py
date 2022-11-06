'''
2022/09/17 daily challenge

learnt from
https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation
'''

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def is_palindrome(w: str):
            return w == w[::-1]
        
        word2idx = {word: idx for idx, word in enumerate(words)}
        pairs = []
        
        for word, idx in word2idx.items():
            wlen = len(word)
            
            for pos in range(0, wlen+1):
                '''
                check if any parts of a word is a palindrome
                in order to determine possible prefixes and suffixes
                which are possible to be paired from other words.
                '''
                prefix = word[:pos]
                suffix = word[pos:]
                
                if is_palindrome(prefix):
                    '''
                    prefix is a palindrome, so its suffix can be reversed
                    and paired with prefix as a palindrome.
                    (reversed suffix + prefix = a palindrome)
                    '''
                    rev_suffix = suffix[::-1]
                    if rev_suffix != word and rev_suffix in word2idx:
                        pairs.append([word2idx[rev_suffix], idx])
                
                if pos != wlen and is_palindrome(suffix):
                    '''
                    check if any suffixes of a word is a palindrome and
                    paired with reversed prefix as a palindrome.
                    (bypass empty suffix because we checked empty prefix
                     which function is equivalent.)
                    (suffix + reversed prefix = a palindrome)
                    '''
                    rev_prefix = prefix[::-1]
                    if rev_prefix != word and rev_prefix in word2idx:
                        pairs.append([idx, word2idx[rev_prefix]])
        
        return pairs
