'''
2024/01/01 daily challenge

greedy method approach
'''


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        
        iter_cookies = iter(s)
        
        content = 0
        for req_size in g:
            for cookie_size in iter_cookies:
                if cookie_size >= req_size:
                    break
            else:
                # no more cookie
                return content
            # child is content with a cookie
            content += 1

        return content

