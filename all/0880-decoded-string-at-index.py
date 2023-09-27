'''
2023/09/27 daily challenge

stack approach
'''

class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        full_length = 0
        
        stack = []  # ('extra word', prev_multiplied_length_plus_current_word, multiplied_full_length)
        word = ''
        for c in s:
            if c.isdigit():
                '''
                append the current word to make a new string after multiplied prefix string
                '''
                prev_plus_word = full_length + len(word)
                '''
                add the current multiplier for the next round of loop
                '''
                full_length = prev_plus_word * int(c)
                stack.append((word, prev_plus_word, full_length))
                
                word_length = 0
                word = ''

                # no need to scan further if exceeds k.
                if full_length > k:
                    break
            else:
                word += c
        
        if word:
            # the last word has no multiplier, push to stack
            full_length += len(word)
            stack.append((word, full_length, full_length))

        #print(str(stack))
        
        while(stack):
            last_word, prev_plus_word, full_length = stack.pop()
            
            '''
            the part of full words within length k can be ignored.
            keep only modulo part of k.
            '''
            k %= prev_plus_word
            
            #print("last=%s, k=%d, next=%s" % (last_word, k, str(stack[-1]) if stack else ''))
            if k == 0 and last_word:
                return last_word[-1]
            
            # check if k is in last_word.
            if stack and last_word and k > stack[-1][2]:
                '''
                if k is longer than the next decoded string,
                the last word is **not** empty,
                k falls in the range of last_word.
                
                if last word _is_ empty, k falls in the next decoded string
                no matter whether k is longer or not.
                '''
                return last_word[k - stack[-1][2] - 1]

        # the leftmost word
        return last_word[k - 1]

