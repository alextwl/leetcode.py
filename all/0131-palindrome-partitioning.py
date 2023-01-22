'''
2023/01/22 daily challenge

dynamic programming + depth first search approach

learnt from official solution
'''

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        dp = [[False] * len(s) for _ in range(len(s))]
        subPalindromes = []  # all subsequences which are valid palindromes
        stack = []  # traversed palindrome group of DFS

        def dfs(start):
            if start >= len(s):
                subPalindromes.append(stack.copy())
            for end in range(start, len(s)):
                '''
                if s[start+1:end] is a palindrome (memorized in dp),
                s[start:end+1] is also a palindrome if s[start] == s[end].

                for all cases in "a", "aa" or "aba" if a subseq when length <= 3 and s[start] == s[end],
                the subseq is identified as a palindrome without checking dp in advance.
                we enable dp memorization here.
                '''
                if (s[start] == s[end]) and (end - start <= 2 or dp[start+1][end-1]):
                    # s[start:end+1] is a palindrome
                    dp[start][end] = True
                    stack.append(s[start:end+1])
                    # traverse deeper from the character (that is s[end+1]) next to the pushed subsequence
                    dfs(end+1)
                    # exit and traverse other branch
                    stack.pop()
            return
        
        # traverse from s[0]
        dfs(0)

        return subPalindromes

