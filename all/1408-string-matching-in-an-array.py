'''
2025/01/07 daily challenge

sorting + brute force approach
'''


class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        words.sort(key=lambda x: -len(x))
        ans = []
        for i, w0 in enumerate(words):
            for j, w1 in enumerate(words):
                if i == j:
                    continue
                if len(w0) <= len(w1):
                    if w0 in w1:
                        ans.append(w0)
                        break
                else:
                    break
        return ans

