'''
2022/08/17 daily challenge
'''
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # [0] -> 'a', ..., [25] -> 'z'
        code = [".-","-...","-.-.","-..",".",
                "..-.","--.","....","..",".---",
                "-.-",".-..","--","-.","---",
                ".--.","--.-",".-.","...","-",
                "..-","...-",".--","-..-","-.--",
                "--.."]
        
        # convert words to an unique SET of morse code representations
        unique_repr = {''.join(code[ord(char) - ord('a')] for char in word)
                       for word in words}
        
        return len(unique_repr)
