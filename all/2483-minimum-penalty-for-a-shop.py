'''
2023/08/29 daily challenge

prefix sum + sort approach
'''


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        n = len(customers)

        '''
        build suffix sum for opening hours
        and prefix sum for closed hours
        '''
        # openSum[i] = accumulated open-hour of penalty for store opening at the i-th hour
        openSum = [0] * (n+1)  # suffix sum
        acc = 0
        for i, c in enumerate(reversed(customers), start=1):
            if c == 'Y':
                acc += 1
            openSum[i] = acc
        openSum.reverse()
        
        # closedSum[i] = accumulated closed-hour of penalty for store closed at the i-th hour
        closedSum = [0] * (n+1)  # prefix sum
        acc = 0
        for i, c in enumerate(customers, start=1):
            if c == 'N':
                acc += 1
            closedSum[i] = acc
        
        # combine the penalty sources for each hours.
        penalties = [a + b for a, b in zip(openSum, closedSum)]
        
        '''
        select the **minimum** penalty (x[1]) with the earliest hour (x[0]) by sorting.
        '''
        return sorted(enumerate(penalties), key=lambda x: (x[1], x[0]))[0][0]

