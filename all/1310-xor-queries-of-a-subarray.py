'''
2024/09/13 daily challenge

prefix XOR approach

since the inputs are large, use a shorter prefix to cancel a longer prefix.
'''


class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        n = len(arr)
        prefix = [0] * (n+1)

        for i, x in enumerate(arr):
            prefix[i+1] = prefix[i] ^ x

        ans = []
        for q0, q1 in queries:
            ans.append(prefix[q0] ^ prefix[q1 + 1])

        return ans

