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


'''
onepass ver
'''


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        earliest = 0
        
        '''
        base case: the penalty when the store closed at the 0-th hour.
        '''
        penalty = min_penalty = customers.count('Y')
        
        for i, c in enumerate(customers):
            '''
            calculate the **next** hour's (== i+1-th hour) penalty
            according to the current i-th hour's status.
            '''
            if c == 'Y':
                penalty -= 1
            else:
                '''
                "the store closed at the i-th hour" means
                the open-hour penalties of i-th & (i+1-th) hours are equal
                and since the store closed at the i-th hour,
                the total penalty of (i+1-th) hour will be one more than i-th hour's.
                '''
                penalty += 1
            
            if penalty < min_penalty:
                min_penalty = penalty
                earliest = i+1  # the earlier hour comes first.

        return earliest

