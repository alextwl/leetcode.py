'''
2022/10/03 daily challenge

intuitive 2-pass

note: official solution provides 1-pass approach
'''

class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        lastColor = None
        sameColorCosts = []  # temp space to memory neededTime(s) of consecutive balloons with same color
        mintime = 0
        
        for color, cost, in zip(colors, neededTime):
            if color == lastColor:
                # consecutive balloons, just memory the cost.
                sameColorCosts.append(cost)
            else:
                # new color approached
                if len(sameColorCosts) > 1:
                    '''
                    consecutive balloons with previous color found,
                    add the sum (without max neededTime) to the overall min time.
                    
                    we may remove multiple balloons and leave 1 ballon eventually.
                    '''
                    mintime += sum(sameColorCosts) - max(sameColorCosts)
                
                # reset memory spaces with new color
                lastColor = color
                sameColorCosts = [cost]
        
        '''
        check if there's consecutive balloons with last color
        '''
        if len(sameColorCosts) > 1:
            mintime += sum(sameColorCosts) - max(sameColorCosts)
        
        return mintime
