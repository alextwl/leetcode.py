'''
2023/08/24 daily challenge
'''

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        output = []
        
        it = iter(words)
        current_line = [next(it)]
        current_width = len(words[0])
        
        for w in it:
            '''
            check if w could be added to current line
            '''
            if current_width + len(w) + 1 > maxWidth:
                # proceed current line
                if len(current_line) > 1:
                    space_per_slot, remaining_spaces = divmod(maxWidth - current_width, len(current_line) // 2)
                    # fill spaces to all slots equally
                    for i in range(1, len(current_line), 2):
                        current_line[i] += ' ' * space_per_slot
                    # fill remaining spaces to slots from left to right
                    i = 1
                    for _ in range(remaining_spaces):
                        current_line[i] += ' '
                        i += 2
                else:
                    # the current line has only single word.
                    current_line.append(' ' * (maxWidth - current_width))

                # submit current line to output
                output.append(''.join(current_line))
                
                # and create a new line.
                current_line = [w]
                current_width = len(w)
            else:
                # append w to current line with a leading space
                current_line.append(' ')
                current_line.append(w)
                current_width += 1 + len(w)
        
        # proceed the last line in left-justified condition.
        if current_width < maxWidth:
            current_line.append(' ' * (maxWidth - current_width))
        output.append(''.join(current_line))

        return output

