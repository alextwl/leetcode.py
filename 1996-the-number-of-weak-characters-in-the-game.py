'''
2022/09/09 daily challenge
learnt from
https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/discuss/2551739/LeetCode-The-Hard-Way-Line-By-Line-Explanation
'''

class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        max_defense = 0
        weak_chars = 0
        
        properties.sort(key=lambda v: (-v[0], v[1]))  # sort attack: descending order, defense: ascending order when attacks were the same.
        
        for attack, defense in properties:
            # the current attack is sorted and always greater or equal to next's attack
            # thus we only check defense value and count it as a weak character.
            if defense < max_defense:
                weak_chars += 1
            else:
                max_defense = defense
        
        return weak_chars
