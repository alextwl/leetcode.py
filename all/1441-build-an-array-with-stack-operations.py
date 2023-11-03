'''
2023/11/03 daily challenge
'''

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        stack = []
        
        prev = 0
        for i in target:
            gap = i - prev - 1
            if gap:
                stack.extend(["Push","Pop"] * gap)
            stack.append("Push")
            prev = i

        return stack

