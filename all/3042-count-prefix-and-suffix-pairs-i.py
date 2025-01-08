'''
2025/01/08 daily challenge

brute force approach
'''


class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        ans = 0
        for i, w0 in enumerate(words):
            for j in range(i+1, n):
                w1 = words[j]
                if w0 == w1[:len(w0)] and w0 == w1[-len(w0):]:
                    ans += 1
        return ans

