'''
2023/07/07 daily challenge

sliding window approach

count the keys within a window and determine if we could flip all T or F in k times.
'''


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        count = {'T': 0, 'F': 0}
        max_len = 0  # the current length of sliding window (also the last valid size of window)
        
        left_iter = iter(answerKey)  # iterate the left pointer if window is invalid
        
        for v in answerKey:
            count[v] += 1
            
            if min(count.values()) <= k:
                '''
                the window can be extended because
                we can flip all T or F in this window within k times.
                '''
                max_len += 1
            else:
                '''
                the window is invalid, while max window size remains,
                let's slide the window (by removing the leftmost key count in the window.)
                '''
                count[next(left_iter)] -= 1

        return max_len

