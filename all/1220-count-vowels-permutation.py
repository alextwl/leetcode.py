'''
2022/08/07 daily challenge

dynamic programming approach

count how many words will end with vowels separately and sum it.

e.g. the next round of words ended with an 'a' will be current words ended in ['e', 'i', 'u'].
'''

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        # last character occurance of words
        a = e = i = o = u = 1
        
        for _ in range(2, n+1):
            a, e, i, o, u =  e+i+u, a+i, e+o, i, i+o
        
        return (a+e+i+o+u) % (10**9 + 7)

