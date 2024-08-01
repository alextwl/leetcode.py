'''
2024/08/01 daily challenge
'''


class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(int(sub[11:13]) > 60 for sub in details)

