'''
2024/07/13 daily challenge
2026/04/01 daily challenge

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


'''
sort only the indices by position values + stack approach
'''


class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        n = len(positions)
        # sort positions' indices by position values
        indices = sorted(range(n), key=lambda x: positions[x])

        stack = []  # robots moving in right direction
        for i in indices:
            if directions[i] == 'R':
                stack.append(i)
            else:
                # robot moving to left found, check collisions
                while stack and healths[i] > 0:
                    if healths[stack[-1]] < healths[i]:
                        # prev robot loses
                        healths[stack.pop()] = 0
                        healths[i] -= 1
                    elif healths[stack[-1]] > healths[i]:
                        # current robot loses
                        healths[stack[-1]] -= 1
                        healths[i] = 0
                    else:
                        # both robots eliminated
                        healths[stack.pop()] = 0
                        healths[i] = 0
        # the problem asks for the health of remaining robots in the order
        # they were given, so just return only positive values of healths[].
        return [h for h in healths if h > 0]

