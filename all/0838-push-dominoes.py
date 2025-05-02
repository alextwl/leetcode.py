'''
2022/09/27 daily challenge
2025/05/02 daily challenge

intuitive: calculate the distances from L & R dominoes
time=O(3n), space=O(2n)

note: more efficient algos are avail from official solutions.
'''

class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        total = len(dominoes)
        
        # distance == -1 means it does not fall to the left/right pushes
        distance2L = [-1] * total
        distance2R = [-1] * total
        
        '''
        count distance from L starting from right bound.
        '''
        distance = -1
        for i, domino in reversed(list(enumerate(dominoes))):
            if domino == 'L':
                distance = 0
            elif domino == 'R':
                # disable distance growth
                distance = -1
            elif distance >= 0:
                # increment distance from L
                distance += 1
                distance2L[i] = distance

        '''
        count distance from R starting from left bound.
        '''
        distance = -1
        for i, domino in enumerate(dominoes):
            if domino == 'R':
                distance = 0
            elif domino == 'L':
                # disable distance growth
                distance = -1
            elif distance >= 0:
                # increment distance from R
                distance += 1
                distance2R[i] = distance
        
        '''
        compare both side of distance and calculate answer
        '''
        ans = list()
        for i, domino in enumerate(dominoes):
            if domino == '.':
                if distance2L[i] >= 0 and distance2R[i] < 0:
                    ans.append('L')
                elif distance2R[i] >= 0 and distance2L[i] < 0:
                    ans.append('R')
                elif distance2L[i] > distance2R[i]:
                    ans.append('R')
                elif distance2L[i] < distance2R[i]:
                    ans.append('L')
                else:
                    ans.append(domino)
            else:
                ans.append(domino)
        
        return ''.join(ans)


'''
finite state machine approach
'''


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        stack = []
        prev_state = '.'
        uprights = 0  # count of dominos whose states are to be determined.

        for c in dominoes:
            if c == '.':
                uprights += 1
            elif c == 'L':
                if prev_state == 'R':
                    # find the centre domino where force is going to be balanced
                    quo, rem = uprights >> 1, uprights & 1
                    stack.append('R' * quo)
                    if rem: stack.append('.')
                    stack.append('L' * quo)
                else:
                    stack.append('L' * uprights)
                uprights = 0
                prev_state = 'L'
                stack.append('L')
            else:
                # c == 'R':
                if uprights:
                    if prev_state == 'R':
                        stack.append('R' * uprights)
                        uprights = 0
                    else:
                        stack.append('.' * uprights)
                        uprights = 0
                prev_state = 'R'
                stack.append('R')

        if uprights:
            stack.append(('R' if prev_state == 'R' else '.') * uprights)

        return ''.join(stack)

