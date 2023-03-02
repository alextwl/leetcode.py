'''
2023/03/02 daily challenge

note the count of any repeating character must be manipulated
as separated single characters of digits.
'''


class Solution:
    def compress(self, chars: List[str]) -> int:
        write_pos = 0  # the position of writer
        prev = chars[0]
        count = 0

        for c in chars:
            if c != prev:
                # the current char is different from the previous,
                # write previous characters to the array

                # write a group of repeating char
                chars[write_pos] = prev
                write_pos += 1
                if (count > 1):
                    for digit in str(count):
                        chars[write_pos] = digit
                        write_pos += 1

                # reset for the new char
                prev = c
                count = 0
            # count the repeating char
            count += 1

        ## proceed the last repeating char
        # write a group of repeating char
        chars[write_pos] = c
        write_pos += 1
        if (count > 1):
            for digit in str(count):
                chars[write_pos] = digit
                write_pos += 1

        # the last position of writer is also the new length of the array        
        return write_pos

