'''
2023/08/03 daily challenge

iterative approach
'''

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        conv = {"2": "abc", "3": "def",
                "4": "ghi", "5": "jkl", "6": "mno",
                "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        letters = [conv[d] for d in digits]
        
        combs = [""]
        for l in letters:
            new_combs = []
            for c in l:
                for prefix in combs:
                    new_combs.append(prefix + c)
            combs = new_combs

        return combs

