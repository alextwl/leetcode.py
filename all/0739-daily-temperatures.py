'''
2022/12/18 daily challenge

the range of the input values is limited and fairly small,
memorizing last seen index does the trick.
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        memorize the reversed index of last seen temperatures.
        the range is limited in 30 <= temperatures[i] <= 100
        '''
        lastseen = [-1] * 102
        ans = []

        for rev, temp in enumerate(reversed(temperatures)):
            lastseen[temp] = rev
            warmer = max(lastseen[temp+1:])  # the nearest reversed index of warmer day
            ans.append(0 if warmer == -1 else rev - warmer)
        
        return ans[::-1]


'''
stack approach
'''

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # value=(reversed index, temperature)
        ans = []

        for rev, temp in enumerate(reversed(temperatures)):
            while(stack and stack[-1][1] <= temp):
                # remove further days which are not warmer than today from stack.
                stack.pop()
            
            # get the distance between nearest warmer day and today.
            ans.append(rev - stack[-1][0] if stack else 0)

            # always push today to the stack to avoid duplicate access to temperatures[].
            stack.append((rev, temp))
        
        return ans[::-1]

