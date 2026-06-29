'''
2026/06/29 daily challenge

built-in pattern matching + oneliner approach
'''


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        return sum(sub in word for sub in patterns)

