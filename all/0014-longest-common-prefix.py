class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        
        for idx in range(0,200):
            try:
                c = strs[0][idx]
            except:
                return prefix
            for txt in strs:
                try:
                    if txt[idx] != c:
                        return prefix
                except:
                    return prefix
            prefix += c

        return prefix


'''
leetcode 75 lv2 day 2

pythonic ver
'''

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp_len = 0

        for chars in zip(*strs):
            #if all([c == chars[0] for c in chars]):
            if len(set(chars)) == 1:
                lcp_len += 1
            else:
                break

        return strs[0][:lcp_len]

