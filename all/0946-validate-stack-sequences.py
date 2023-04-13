'''
2023/04/13 daily challenge

just simulate if the operations were possible.

there's always most 1 path is valid due to various constraints,
so no need to try every branch from each decision recursively (and it will TLE.)
'''

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        plen = len(pushed)
        stack = []
        next_pop = 0

        for v in pushed:
            # try push
            stack.append(v)
            # try pop as much as possible
            while(stack and stack[-1] == popped[next_pop]):
                stack.pop()
                next_pop += 1
        
        # in the end of loop the stack must be empty
        return not stack

