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


'''
easier 1-pass approach
time=O(N), space=O(1)
'''

class Solution2:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        lastColor = None
        colorMaxtime = 0
        mintime = 0
        
        for color, cost, in zip(colors, neededTime):
            # always add cost to mintime regardless of consecutive status.
            mintime += cost
            
            if color == lastColor:
                # consecutive balloons, just memory the max cost.
                colorMaxtime = max(colorMaxtime, cost)
            else:
                '''
                new color approached
                
                no matter whether there were consecutive balloons with same color or not,
                just subtract mintime with last maximum neededTime
                because we always keep the balloon with max cost.
                
                although there's single ballon with previous color,
                we don't remove it so we also subtract its cost (== colorMaxtime) from mintime.
                '''
                mintime -= colorMaxtime
                
                # reset with new color
                lastColor = color
                colorMaxtime = cost
        
        '''
        always subtract last max cost with last color
        '''
        mintime -= colorMaxtime
        
        return mintime
