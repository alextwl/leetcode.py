'''
2023/07/01 daily challenge

depth first search approach
'''

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        dist = [0] * k
        n = len(cookies)
        
        def dfs(i, zero_cookies_child):
            '''
            :param i: the index of bag cookies[i] to be distributed
            :param zero_cookies_child: the count of children who got zero cookies
            :return: the unfairness of current distribution
            '''
            if n - i < zero_cookies_child:
                '''
                early stopper:
                if the remaining bags of cookies were insufficient and 
                there's at least one or more children will get zero cookies,
                the answer will be invalid because the constraint 2 <= k <= cookies.length
                guarantees each child should get at least one bag for optimal answer.
                '''
                return float('inf')
            
            # all bags of cookies distributed, return the unfairness == the maximum cookies
            if i == n:
                return max(dist)

            # distribute the current bag and the remaining bags
            current_bag = cookies[i]
            
            ans = float('inf')
            for child in range(k):
                if dist[child] == 0:
                    zero_cookies_child -= 1  # because we are going to distribute a bag to him/her.

                dist[child] += current_bag
                ans = min(ans, dfs(i+1, zero_cookies_child))
                
                # rollback the distribution
                dist[child] -= current_bag
                if dist[child] == 0:
                    zero_cookies_child += 1

            return ans
        
        # distribute the first bag with all children having no cookies.
        return dfs(0, k)

