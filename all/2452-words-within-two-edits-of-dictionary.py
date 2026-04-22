'''
2026/04/22 daily challenge

brute force approach
'''


class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        ans = []
        for q in queries:
            found = False
            for w in dictionary:
                edits = 0
                for a, b in zip(q, w):
                    if a != b:
                        edits += 1
                    if edits > 2:
                        break
                else:
                    found = True
                if found:
                    ans.append(q)
                    break
        return ans

