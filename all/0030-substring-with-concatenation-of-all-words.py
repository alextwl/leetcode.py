'''
2022/08/13 daily challenge

sliding window approach

learnt from official solution
'''

import collections


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        n = len(s)
        size_words = len(words)
        len_word = len(words[0])
        len_substr = len_word * size_words
        
        count_words = collections.Counter(words)
        
        ans = []
        # the number of sliding windows is equal to the length of a single word.
        for i in range(0, len_word):
            found_words = collections.deque()
            remaining_words = dict(count_words)
            
            for j in range(i, n-len_word+1, len_word):
                w = s[j:j+len_word]
                if (rem := remaining_words.get(w, -1)) > 0:
                    '''
                    rem =
                    -1: word not found
                     0: word found but the remaining quota is exhausted
                    >0: word found and can be added to the current substring
                    '''
                    remaining_words[w] -= 1
                    found_words.append(w)
                    
                    # check if it formed a complete substring or not.
                    if len(found_words) == size_words:
                        # add the beginning of substring to answer
                        ans.append(j - len_substr + len_word)
                        # pop the earlist word found in the current substring
                        # for the next possible string in the current sliding window.
                        remaining_words[found_words.popleft()] += 1
                elif rem == 0:
                    '''
                    word found in the previous if-condition
                    but the remaining quota is exhausted.
                    '''
                    while (found_words):
                        '''
                        the substring finding can resume without disruption
                        if the current word was already found in found_words.
                        '''
                        old = found_words.popleft()
                        if old == w:
                            found_words.append(w)
                            break
                        else:
                            remaining_words[old] += 1
                else:
                    # word not found, restart for a new round of substring finding.
                    found_words = collections.deque()
                    remaining_words = dict(count_words)

        return ans

