'''
2024/10/04 daily challenge

sorting approach
'''


class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()

        team_skill = skill[0] + skill[-1]
        chemistry = 0

        for a, b in zip(skill, skill[:len(skill)//2-1:-1]):
            if a + b != team_skill:
                return -1
            chemistry += a * b

        return chemistry

