'''
2022/10/24 daily challenge

DFS backtracing approach

it's actually a kind of bruteforce method,
however since the unique characters are limited in 26 alphabets,
the answer can be evaluated within limited runtime.
'''

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def dfs(start: int, word: str):
            '''
            :param start: the index of word to start searching.
            :param word: the string of previous concatenacted words.
            '''
            
            '''
            the problem does not guarantee all characters in a word of arr[] are unique,
            this verifies the word to meet the requirement.
            '''
            if len(set(word)) != len(word):
                # the word itself has duplicate characters, is invalid to be concatenated.
                return 0
            
            # the length of the word itself may be also the maximum length of answer.
            maxlen = len(word)
            
            for i in range(start, len(arr)):
                # try to concatenate with the next word.
                maxlen = max(maxlen, dfs(i+1, word + arr[i]))
            
            return maxlen
        
        # the empty string may be also the maximum length of answer, so we start searching with it.
        return dfs(0, "")
