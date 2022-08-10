'''
Implement strStr by KMP

Time=O(m*n), space=O(1)

learnt from
https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
'''
def get_lps(pat: str) -> list:
    '''
    Generate longest proper prefix (also suffix)
    '''
    patlen = len(pat)
    lps = [0] * patlen

    for i in range(1, patlen):
        # search subpattern
        sublen = i+1
        sub = pat[:sublen]
        for j in range(1, sublen):
            if sub[:j] == sub[-j:]:
                # save max length of substring to lps
                lps[i] = j

    return lps


def kmp(txt: str, pat: str) -> int:
    '''
    Knuth-Morris-Pratt (KMP) String Matching Algorithm
    '''
    lps = get_lps(pat)
    txtlen = len(txt)
    patlen = len(pat)

    i = j = 0
    while(i < txtlen):
        if j == patlen:
            # pattern matches
            return i - j
        if txt[i] == pat[j]:
            i += 1
            j += 1
        elif j > 0:
            # current subpattern mismatch, reset j to previous lps
            j = lps[j-1]
        else:
            # all subpattern mismatch, go next char of input
            i += 1

    if j == patlen:
        # pattern == suffix of input case
        return i - j
    # pattern mismatch
    return -1


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return kmp(haystack, needle)

