'''
2025/01/02 daily challenge

prefix sum approach
'''


class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefix = [0]
        curr_sum = 0
        for w in words:
            if w[0] in ['a', 'e', 'i', 'o', 'u'] and w[-1] in ['a', 'e', 'i', 'o', 'u']:
                curr_sum += 1
            prefix.append(curr_sum)

        ans = []
        for i, j in queries:
            ans.append(prefix[j+1] - prefix[i])
        return ans

