'''
2023/09/14 daily challenge

Euler path finding + DFS approach (recursive ver)
'''

import collections


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:        
        # dep2arr[airport of departure] = [destinations of airport, ...]
        dep2arr = collections.defaultdict(list)
        itinerary = []
        
        # convert tickets to dep2arr and sort it in lexical order
        # (reversed for recursive dfs implementation)
        for departure, arrival in tickets:
            dep2arr[departure].append(arrival)
        for departure in dep2arr.keys():
            dep2arr[departure] = sorted(dep2arr[departure], reverse=True)
        
        def dfs(departure):
            nonlocal dep2arr, itinerary
            while(dep2arr[departure]):
                next_destination = dep2arr[departure].pop()
                dfs(next_destination)
            # no more itineraries departed from the input airport.
            # time to push it to the reconstructed itinerary.
            itinerary.append(departure)
        
        # search from JFK
        dfs("JFK")
        # reverse the final answer because it's appended from terminal to beginning airport.
        return itinerary[::-1]


'''
Euler path finding + DFS approach (stack ver)
'''

import collections


class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:        
        # dep2arr[airport of departure] = [destinations of airport, ...]
        dep2arr = collections.defaultdict(list)
        itinerary = []
        
        # convert tickets to dep2arr and sort it in lexical order
        # (reversed for recursive dfs implementation)
        for departure, arrival in tickets:
            dep2arr[departure].append(arrival)
        for departure in dep2arr.keys():
            dep2arr[departure] = sorted(dep2arr[departure], reverse=True)
        
        # search from JFK
        stack = ["JFK"]
        
        while(stack):
            departure = stack[-1]
            if dep2arr[departure]:
                # queue next destination
                stack.append(dep2arr[departure].pop())
            else:
                # no more itinearaies departed from the current airport.
                # time to append it to the final itinerary
                itinerary.append(stack.pop())
        
        # reverse the final answer because it's appended from terminal to beginning airport.
        return itinerary[::-1]

