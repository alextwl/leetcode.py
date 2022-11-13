'''
2022/11/13 daily challenge

pythonic oneliner
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        # the inline loop is to kill leading, trailing, and duplicate spaces.
        return ' '.join(sub for sub in reversed(s.split(' ')) if sub)


'''
manual approach: multipass swapping

surprisingly its actual runtime is shorter than the oneliner's...
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        # convert s to mutable list for swapping
        s = list(s)
        
        '''
        find the indexes of non-space beginning and end of s.
        it kills leading & trailing spaces.
        '''
        begin, end = 0, len(s) - 1
        for c in range(0, end + 1):
            if s[c] != ' ':
                break
            begin += 1
        for c in range(end, -1, -1):
            if s[c] != ' ':
                break
            end -= 1
        
        # kill the duplicate spaces between words
        i = j = begin
        while(j <= end):
            if s[j] == ' ':
                # keep single space
                s[i] = ' '
                i += 1
                # forward j to non-space char.
                while(s[j] == ' '):
                    j += 1
                    if j == end:
                        break
            s[i] = s[j]
            i += 1
            j += 1
        # renew non-space end of s
        end = i - 1
        
        # reverse the entire s[begin:end+1]
        left, right = begin, end
        while(left < right):
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        
        # print(''.join(s[begin:end+1]))
        
        # reverse each word
        idx = begin
        while(idx <= end):
            if s[idx] != ' ':
                # find the left & right pointer from each terminal of a word
                wl = wr = idx
                while(wr <= end and s[wr] != ' '):
                    wr += 1
                wr -= 1 # move left by 1 because s[wr] is a space or overflowed.
                # save the index end of the word to idx in advance.
                idx = wr
                # reverse the chars of the word.
                while(wl < wr):
                    s[wl], s[wr] = s[wr], s[wl]
                    wl += 1
                    wr -= 1
            # continue to next word
            idx += 1
        
        return ''.join(s[begin:end+1])

