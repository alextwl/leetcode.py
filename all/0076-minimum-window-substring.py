'''
2022/10/22 daily challenge

simple sliding window approach

learnt from the official solution
'''

import collections


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # build a counter dict for all characters in target t.
        t_counts = collections.Counter(t)
        
        # the number of unique characters in target t.
        unique_t_len = len(t_counts)
        
        # the number of unique characters in target t found in the current window.
        unique_t_found = 0
        
        # the counter of any character found in the current window.
        c_counts = collections.Counter()
        
        # the length, left & right pointers of the minimum window.
        min_window_len = float('inf')
        min_window_left = min_window_right = None
        
        # runtime window pointers
        left = right = 0
        
        while right < len(s):
            c = s[right]
            
            '''
            add count of current character no matter whether the char is in t or not.
            we'll move left pointer later only if all required characters in t found in the current window.
            '''
            c_counts[c] += 1
            
            if c in t_counts and c_counts[c] == t_counts[c]:
                # required number of an unique characters in t found in the current window.
                unique_t_found += 1
            
            '''
            time to minimize current window if all t chars found.
            '''
            while left <= right and unique_t_found == unique_t_len:
                # update the minimum window length and range first.
                window_len = right - left + 1
                if window_len < min_window_len:
                    min_window_len = window_len
                    min_window_left, min_window_right = left, right
                
                # try to remove the char of left pointer
                c = s[left]
                c_counts[c] -= 1
                if c in t_counts and c_counts[c] < t_counts[c]:
                    '''
                    if c was a char in the target, subtract the unique t counter
                    and the loop ends in this round. (fallback to expand right pointer later)
                    '''
                    unique_t_found -= 1
                
                # expand left pointer to shrink the current window.
                left += 1
            
            # expand right pointer and the current window.
            right += 1
        
        if min_window_len == float('inf'):
            # insufficient target characters found.
            return ""
        
        # the string of the minimum window found.
        return s[min_window_left: min_window_right+1]
