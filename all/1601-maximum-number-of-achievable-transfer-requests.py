'''
2023/07/02 daily challenge

depth first search approach
'''

class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        indegree = [0] * n  # the indegree of each building
        ans = 0
        
        def dfs(pos: int, req_count: int):
            '''
            :param pos: the index of a request we are going to proceed.
            :param req_count: the count of achieved requests.
            '''
            nonlocal ans

            if pos == len(requests):
                # all requests proceeded, check if indegrees of all buildings were equal to zero or not.
                if not any(indegree):
                    '''
                    the combination of requests can be achieved
                    because all buildings are just full,
                    we can update the maximum achievable transfer request count.
                    '''
                    ans = max(ans, req_count)
                return
            
            # accept the request
            src, dst = requests[pos]
            indegree[src] -= 1
            indegree[dst] += 1
            dfs(pos+1, req_count+1)
            
            # rollback and reject the request
            indegree[src] += 1
            indegree[dst] -= 1
            dfs(pos+1, req_count)

        # start from the first request with no requests proceeded.
        dfs(0, 0)
        return ans

