'''
2025/06/04 daily challenge

brute-force method approach

time=O(n**2)
'''


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        n = len(word)
        max_len = n - numFriends + 1
        largest = ""
        for i in range(n):
            # built-in string comparsion is lexicographical.
            largest = max(largest, word[i:min(i+max_len, n)])
        return largest


'''
two pointers (proof by contradiction) approach

learnt from official editorial 2:
https://leetcode.com/problems/find-the-lexicographically-largest-string-from-the-box-i/editorial/#approach-2-two-pointers
'''


def last_sub(s):
    # find the suffix containing the largest lexicographical substring.
    n = len(s)
    i, j = 0, 1  # the pointers where Si & Sj starting at
    while j < n:
        k = 0
        while j+k < n and s[i+k] == s[j+k]:
            k += 1
        if j+k < n and s[i+k] < s[j+k]:
            # Sj is larger than Si in length k.
            # Sj becomes the new Si, is going to compare the next substring.
            i, j = j, max(j+1, i+k+1)
        else:
            # Si is equal to or larger than Sj.
            j += k + 1
    return s[i:]


class Solution:
    def answerString(self, word: str, numFriends: int) -> str:
        if numFriends == 1:
            return word
        sub = last_sub(word)
        return sub[:min(len(sub), len(word) - numFriends + 1)]

