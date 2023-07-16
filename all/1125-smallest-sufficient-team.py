'''
2023/07/16 daily challenge

dynamic programming + bitmask approach

learnt from the official solution 1
https://leetcode.com/problems/smallest-sufficient-team/solution/
'''

import functools


class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        m = len(req_skills)
        n = len(people)

        '''
        build a 'skill name to bitmask' dict.
        '''
        skill2bin = {skill_name: 1 << i for i, skill_name in enumerate(req_skills)}
        '''
        convert people skill lists to bitmask.
        '''
        people2bin = [functools.reduce(lambda x, y: x | skill2bin[y], skill_list, 0) for skill_list in people]
        
        '''
        do dynamic programming: try to miminize the team for each skill set
        '''
        # the bitmask of all people
        all_people_bin = (1 << n) - 1
        # dp[skill_mask] = the minimal people_mask
        dp = [all_people_bin] * (1 << m)
        dp[0] = 0
        
        for team_skills in range(1, 1 << m):
            for i, ppl_skills in enumerate(people2bin):
                # test if the people possesses the skill needed for the current team skill mask
                smaller_team_skills = team_skills & ~ppl_skills
                if smaller_team_skills != team_skills:
                    '''
                    the people has skills that's included in the team,
                    we may find a smaller team + the current person
                    from the smaller set of skills
                    '''
                    new_team = dp[smaller_team_skills] | (1 << i)
                    if new_team.bit_count() < dp[team_skills].bit_count():
                        # a smaller team with the current skills is found.
                        dp[team_skills] = new_team
        
        ans_team_bin = dp[-1]
        ans = [i for i in range(n) if ans_team_bin & (1<<i)]

        return ans

