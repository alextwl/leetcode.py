'''
2024/07/14 daily challenge

stack + counter approach
'''

import collections


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack_dict = [collections.Counter()]
        
        # stacks for atom name and quantizer in single chars
        atom_name = []
        quantizer = []
        
        prev = ""
        for v in formula:
            if v.isdigit():
                quantizer.append(v)
            elif v.islower():
                atom_name.append(v)
            else:
                #if v.isupper() or v == ')':
                # convert the last atom
                if prev == ')':
                    # close the last parenthesis and append to upper level's counter
                    ctr = stack_dict.pop()
                    stack_dict[-1] += ctr
                elif atom_name:
                    stack_dict[-1][''.join(atom_name)] += int(''.join(quantizer)) if quantizer else 1
                elif quantizer:
                    # atom_name is empty but quantizer exists means it's a quantizer for a parenthesis
                    ctr = stack_dict.pop()
                    multiplier = int(''.join(quantizer))
                    for a, q in ctr.items():
                        stack_dict[-1][a] += q * multiplier
                # clean up
                atom_name = list()
                quantizer = list()
                
                if v == '(':
                    stack_dict.append(collections.Counter())
                elif v.isupper():
                    atom_name.append(v)
            #
            prev = v
        
        # proceed the last atom
        if prev.isalpha():
            stack_dict[-1][''.join(atom_name)] += 1
        elif prev == ')':
            # close the last parenthesis and append to upper level's counter
            ctr = stack_dict.pop()
            stack_dict[-1] += ctr
        elif atom_name:
            stack_dict[-1][''.join(atom_name)] += int(''.join(quantizer)) if quantizer else 1
        elif quantizer:
            # atom_name is empty but quantizer exists means it's a quantizer for a parenthesis
            ctr = stack_dict.pop()
            multiplier = int(''.join(quantizer))
            for a, q in ctr.items():
                stack_dict[-1][a] += q * multiplier

        # serialize the answer string
        ans = []
        last_ctr = stack_dict[-1]
        for a in sorted(last_ctr.keys()):
            ans.append(a)
            if last_ctr[a] > 1:
                ans.append(str(last_ctr[a]))

        return ''.join(ans)

