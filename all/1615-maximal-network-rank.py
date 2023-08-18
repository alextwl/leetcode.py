'''
2023/08/18 daily challenge
'''

import collections

class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        degrees = [0] * n
        g = collections.defaultdict(set)
        
        for a, b in roads:
            degrees[a] += 1
            degrees[b] += 1
            g[a].add(b)
            g[b].add(a)
        
        city_degree = sorted([(c, d) for c, d in enumerate(degrees)], key=lambda x:x[1])
        
        '''
        pick cities with biggest degrees,
        if there are more than one city,
        we can just evaluate pairs from these cities. 
        '''
        max_degree = city_degree[-1][1]
        biggest_cities = []
        while(city_degree):
            if city_degree[-1][1] == max_degree:
                biggest_cities.append(city_degree.pop()[0])
            else:
                break
        
        if len(biggest_cities) == 1:
            '''
            there's only one biggest city which is not enough,
            we pick second biggest cities for more pairs.
            '''
            second_degree = city_degree[-1][1]
            while(city_degree):
                if city_degree[-1][1] == second_degree:
                    biggest_cities.append(city_degree.pop()[0])
                else:
                    break
        else:
            second_degree = max_degree

        almost_max_rank = max_degree + second_degree
        for i in range(len(biggest_cities)):
            for j in range(i+1, len(biggest_cities)):
                a, b = biggest_cities[i], biggest_cities[j]
                if b not in g[a] and degrees[a] + degrees[b] == almost_max_rank:
                    '''
                    city a & b are not directly connected and have the sum of the almost max rank,
                    we can safely return it.
                    '''
                    return almost_max_rank

        return almost_max_rank - 1

