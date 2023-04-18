'''
2023/04/18 daily challenge
'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1, n2 = len(word1), len(word2)

        ans = ""
        for i in range(min(n1, n2)):
            ans += word1[i] + word2[i]

        if (diff := n1-n2) > 0:
            ans += word1[-diff:]
        elif (diff := n2-n1) > 0:
            ans += word2[-diff:]

        return ans

