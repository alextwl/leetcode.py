'''
2024/07/13 daily challenge

sorting + stack approach

similar to problem 735 Asteroid Collision.
'''


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        pairs = [(pos, hp, arrow == 'R', idx)
                    for idx, (pos, hp, arrow) in
                        enumerate(zip(positions, healths, directions))]
        pairs.sort()

        survived = []  # [idx, hp]
        stack = []  # [idx, hp], stores only robots moving to the right
        for pos, hp, to_right, idx in pairs:
            if to_right:
                # moving to the right side
                stack.append([idx, hp])
            else:
                # moving to the left side
                while(stack):
                    opponent_hp = stack[-1][1]
                    if hp == opponent_hp:
                        # both robots removed
                        stack.pop()
                        break
                    elif hp > opponent_hp:
                        # opponent removed
                        stack.pop()
                        hp -= 1
                    else:
                        # opponent > hp
                        # the current robot removed
                        stack[-1][1] -= 1
                        break
                else:
                    if hp > 0:
                        # no more robots in the stack, the robot is survived
                        survived.append([idx, hp])
        
        # robots remaining in the stack are also survived
        survived.extend(stack)
        survived.sort()

        return [hp for _, hp in survived]

